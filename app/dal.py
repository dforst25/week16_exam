import pymongo

from connection import MongoConnector
import os

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "employees")
CNX = MongoConnector()


def get_engineering_high_salary_employees():
    employees = CNX.get_coll(COLLECTION_NAME)
    filtered_emp = employees.find({"job_role.department": "Engineering", "salary": {"$gt": 65000}},
                                  {'_id': 0, 'employee_id': 1, 'name': 1, 'salary': 1})
    return list(filtered_emp)


def get_employees_by_age_and_role():
    employees = CNX.get_coll(COLLECTION_NAME)
    filtered_emp = employees.find(
        {"job_role.title": {"$in": ["Engineer", "Specialist"]}, "age": {"$gte": 30, "$lte": 45}},
        {'_id': 0})
    return list(filtered_emp)


def get_top_seniority_employees_excluding_hr():
    employees = CNX.get_coll(COLLECTION_NAME)
    filtered_emp = employees.find(
        {"job_role.department": {"$not": {"$regex": "HR"}}},
        {'_id': 0}).sort([("years_at_company", pymongo.DESCENDING)]).limit(7)
    return list(filtered_emp)


def get_employees_by_age_or_seniority():
    employees = CNX.get_coll(COLLECTION_NAME)
    filtered_emp = employees.find({"$or": [{"years_at_company": {"$lt": 3}}, {"age": {"$gt": 50}}]},
                                  {'_id': 0, 'employee_id': 1, 'name': 1, 'age': 1, 'years_at_company': 1})
    return list(filtered_emp)
