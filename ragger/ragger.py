from . import data_manager


class ContextSearch:
    def __init__(self):
        self.data_manager = data_manager.DataManager()

    def submit(self, path):
        directories = self.data_manager.insert(path)
        self.data_manager.insert(directories)

    def retrive(self, query):

        


class Ragger(ContextSearch):
    def __init__(self):
        super().__init__()

    def retrive(self, context):
        pass
