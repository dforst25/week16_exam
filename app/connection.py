from pymongo import MongoClient
import os
from init_db import init_db_and_coll


class MongoConnector:
    def __init__(self):
        self.db_name = os.getenv("DATABASE_NAME", "employee_db")
        self.mongo_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017/")
        self.client = None

    def init_db(self):
        init_db_and_coll(self.mongo_url, self.db_name)

    def get_client(self):
        if self.client is None:
            self.client = MongoClient(self.mongo_url)
            self.client.admin.command('ping')

            if self.db_name not in self.client.list_database_names():
                self.init_db()
        return self.client

    def get_db(self):
        return self.get_client()[self.db_name]

    def get_coll(self, coll_name):
        return self.get_db()[coll_name]

    def check_connection(self):
        if self.client is None:
            raise ConnectionError("Server not connected")
        else:
            self.client.admin.command('ping')
