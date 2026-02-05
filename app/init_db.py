from pymongo import MongoClient
import json
import os

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "employees")


def insert_from_json_to_mongodb(json_path, collection_name, mongodb):
    print("perfect")
    with open(json_path) as file:
        data = json.load(file)
        mongodb[collection_name].insert_many(data)


def init_db_and_coll(mongodb_url: str, db_name):
    client = MongoClient(mongodb_url)
    db = client[db_name]
    file_name = "employee_data_advanced.json"
    insert_from_json_to_mongodb(file_name, COLLECTION_NAME, db)
