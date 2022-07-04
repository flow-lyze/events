from . database import Database

import pymongo
from bson.objectid import ObjectId

from models.api import Event


class MongoConnection:

    def __init__(self, credentials):
        self.__credentials = credentials
        self.__connection = self.__get_connection()

    def __enter__(self):
        return self.__connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.close()

    def __get_connection(self):
        client = pymongo.MongoClient(self.__credentials["host"], self.__credentials["port"])
        return client

    def __heart_beat(self):
        self.__connection.server_info()


class Mongo(Database):

    KEY = "mongo"

    def __init__(self, db=None, collection=None):
        super().__init__(self.KEY)
        self.__db = db or self._secrets["db"]
        self.__collection = collection or self._secrets["events_collection"]

        # by default, port comes as string
        self._secrets["port"] = int(self._secrets["port"])

    def get_record(self, search_filter):
        with MongoConnection(self._secrets) as connection:
            record = connection[self.__db][self.__collection].find_one(search_filter)
            return record

    def batch_get_records(self, search_filter):
        with MongoConnection(self._secrets) as connection:
            cursor = connection[self.__db][self.__collection].find(search_filter)
            records = [rec for rec in cursor]
            return records

    def create_new_record(self, data):
        with MongoConnection(self._secrets) as connection:
            collection = connection[self.__db][self.__collection]
            collection.insert_one(data)

    def delete_record(self, data):
        with MongoConnection(self._secrets) as connection:
            collection = connection[self.__db][self.__collection]
            collection.delete_one(data)

    def edit_record(self, event_to_update: Event):
        with MongoConnection(self._secrets) as connection:
            collection = connection[self.__db][self.__collection]

            event_to_update = dict(event_to_update)
            event_id = event_to_update.pop("id")
            result = collection.update_one(
                {"_id": ObjectId(event_id)},
                {"$set": event_to_update}
            )

            return result

    def batch_create_records(self):
        raise NotImplemented

    def batch_delete_records(self):
        raise NotImplemented

    def batch_edit_records(self):
        raise NotImplemented

    def __repr__(self):
        super().__repr__()
