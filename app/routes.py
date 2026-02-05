from fastapi import APIRouter, HTTPException
import dal

router = APIRouter()


@router.get("/employees/engineering/high-salary")
def get_high_salary_employees():
    try:
        return dal.get_engineering_high_salary_employees()
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"can't get the high salary employees \n{str(e)}")


@router.get("/employees/by-age-and-role")
def get_employees_by_age_and_role():
    try:
        return dal.get_employees_by_age_and_role()
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"can't filtered the employees by age and role \n{str(e)}")


@router.get("/employees/top-seniority")
def get_high_salary_employees():
    try:
        return dal.get_top_seniority_employees_excluding_hr()
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"can't get the top seniority employees \n{str(e)}")


@router.get("/employees/age-or-seniority")
def get_high_salary_employees():
    try:
        return dal.get_employees_by_age_or_seniority()
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"can't filtered the employees by age or seniority\n{str(e)}")


@router.get("/employees/managers/excluding-departments")
def get_high_salary_employees():
    try:
        return dal.get_managers_excluding_departments()
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"can't filtered the managers employees \n{str(e)}")


@router.get("/employees/by-lastname-and-age")
def get_high_salary_employees():
    try:
        return dal.get_employees_by_lastname_and_age()
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"can't filtered the employees by lastname and age\n{str(e)}")
