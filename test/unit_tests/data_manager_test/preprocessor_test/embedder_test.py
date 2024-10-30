from context_search.preprocessor.embedder import TextEmbedder
from context_search.data_classes import Embeddable
import pytest
import numpy as np
import random


random.seed(0)
np.random.seed(0)

text_to_embed = "This is a test text. This is a test text. This is a test text."


def test_creating_embeddings_from_text():
    embedder = TextEmbedder()
    embedding = embedder.embed(text_to_embed)

    assert pytest.approx(embedding[0], 1e-3) == np.load(
        "test/unit_tests/data_manager_test/preprocessor_test/test_embedding.npy"
    )


def test_creating_embeddings_from_multiple_texts():
    embedder = TextEmbedder()
    chunk_1 = Embeddable(text=text_to_embed)
    chunk_2 = Embeddable(text=text_to_embed)

    embeddings = embedder.produce_embeddings([chunk_1, chunk_2])

    assert pytest.approx(embeddings[0][0], 1e-3) == np.load(
        "test/unit_tests/data_manager_test/preprocessor_test/test_embedding.npy"
    )

    assert pytest.approx(embeddings[1][0], 1e-3) == pytest.approx(embeddings[0][0], 1e-3)
