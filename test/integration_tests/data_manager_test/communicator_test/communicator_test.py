import pytest

from context_search.communicator import CommAdapterNeo
from context_search.data_classes import Literature
from context_search.communicator.query_builder import QueryBuilder


class TestCommunicatorConnection:
    def setup_test(test):
        test.uri = "neo4j://database:7687"
        test.user = "neo4j"
        test.password = "StrongPsPsP5"
        test.communicator = None

    def test_communicator_creation(test):
        test.setup_test()
        test.communicator = CommAdapterNeo(test.uri, test.user, test.password)
        assert test.communicator is not None
        test.communicator = None


class TestCommunicatorTransactions:
    def setup_test(test):
        test.uri = "neo4j://database:7687"
        test.user = "neo4j"
        test.password = "StrongPsPsP5"
        test.communicator = CommAdapterNeo(test.uri, test.user, test.password)
        test.literature = Literature(
            filename="test",
            filepath="test"
        )

    def test_add_literature(test):
        test.setup_test()
        test.session = test.communicator.driver.session(database="neo4j")
        test.session.execute_write(
            QueryBuilder._merge_literature,
            test.literature
        )
        test.session.close()

    @pytest.mark.dependency(depends=["test_add_literature"])
    def test_get_literature(test):
        test.setup_test()
        test.session = test.communicator.driver.session(database="neo4j")
        test.session.execute_write(
            QueryBuilder._merge_literature,
            test.literature
        )
        literature = test.communicator.get_literature("test")
        test.session.close()
        assert literature is not None

    @pytest.mark.dependency(depends=["test_add_literature"])
    def test_get_all_literatures(test):
        test.setup_test()
        test.session = test.communicator.driver.session(database="neo4j")
        test.session.execute_write(
            QueryBuilder._merge_literature,
            test.literature
        )
        literatures = test.communicator.get_all_literatures()
        test.session.close()
        assert len(literatures) > 0

    # @pytest.mark.dependency(depends=["test_add_literature"])
    # def test_delete_literature(test):
    #     test.setup_test()
    #     test.communicator.add_literature(test.literature)
    #     test.communicator.delete_literature("test")
    #     assert test.communicator.get_literature("test") is None
