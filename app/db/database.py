from abc import ABC, abstractmethod

from .. configs import conf


CONFIG = conf.Config().CONFIG


class DatabaseException(Exception):
    pass


class Database(ABC):

    """Base Interface for inheritance and implementation DB methods."""

    def __init__(self, key, *args, **kwargs):
        self._secrets = CONFIG[key]

    @abstractmethod
    def get_record(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_new_record(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_record(self, *args, **kwargs):
        pass

    @abstractmethod
    def edit_record(self, *args, **kwargs):
        pass

    @abstractmethod
    def batch_get_records(self, *args, **kwargs):
        pass

    @abstractmethod
    def batch_create_records(self, *args, **kwargs):
        pass

    @abstractmethod
    def batch_delete_records(self, *args, **kwargs):
        pass

    @abstractmethod
    def batch_edit_records(self, *args, **kwargs):
        pass

    def __repr__(self):
        return """Database Interface - is basic point of building different
                  db hierarchies.
            
                  All abstract methods should be derived and implemented.
                  Usually, methods are useful CRUD operations, that are used in every day routine,
                  The idea of this, is to create custom ORM for different databases.
                  """


