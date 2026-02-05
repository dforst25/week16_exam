from connection import MongoConnector
import os

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "employees")
CNX = MongoConnector()


def get_engineering_high_salary_employees():
    employees = CNX.get_coll(COLLECTION_NAME)
    filtered_emp = employees.find({"job_role.department": "Engineering", "salary": {"$gt": 65000}},
                                  {'_id': 0, 'employee_id': 1, 'name': 1, 'salary': 1})
    return filtered_emp
