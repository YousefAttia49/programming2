from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Front_End:
    def __init__(self, data_source):
        data = self.data_source.get_data()
        print('Display Data', data)


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"
    

