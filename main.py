#Python
from typing import Optional, List
from uuid import UUID
from datetime import date
from datetime import datetime
import json

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body
from fastapi import Path
from fastapi import HTTPException

app = FastAPI()

#Models
class Vacancy(BaseModel):
    vacancy_id : int = Field(
        ...,
        gt=0
    )

    position_name : str = Field(
        ...,
        min_length=1
    )
    vacancy_link : str = Field(
        ...,
        min_length=1
    )
    company_id : int = Field(
        ...,
        gt=0
    )

    salary : int = Field(
        ...,
        gt=0
    )

    skills : str = Field(
        ...,
        min_length=1
    )
    
    max_experience : int = Field(
        ...,
        ge=0
    )
    min_experience : int = Field(
        ...,
        ge=0
    )

class Company(BaseModel):

    company_id : int = Field(
        ...,
        gt=0
    )

    company_name : str = Field(
        ...,
        min_length=1
    )

    link : str = Field(
        ...,
        min_length=1
    )

    country : str = Field(
        ...,
        min_length=1
    )

    city : str = Field(
        ...,
        min_length=1
    )

    date_added : date = Field(
        default=date.today()
    )

    contact_first_name : str = Field(
        ...,
        min_length=1
    )

    contact_last_name : str = Field(
        ...,
        min_length=1
    )

    contact_phone_number : str = Field(
        ...,
        min_length=11,
        max_length=11
    )

    contact_email : str = EmailStr(
        ...
    )

@app.get(
    path="/vacancies/{vacancy_id}",
    response_model= Vacancy,
    status_code = status.HTTP_200_OK,
    summary="Show one Vacancy",
    tags=["Vacancy"]
)
def show_vacancy(vacancy_id: int = Path(
    ...,
    ge=1,
    title="Vacancy ID",
    description="This is the vacancy ID",
    example= 1
    )):
    with open("vacantes.json", 'r', encoding="utf-8") as f:
        results = json.loads(f.read())
        id = vacancy_id
    for data in results:
        if data["vacancy_id"] == id:
            return data
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"¡This vacancy_id doesn't exist!"
        )


@app.get(
    path="/companies/{company_id}",
    response_model= Company,
    status_code = status.HTTP_200_OK,
    summary="Show one Company",
    tags=["Company"]
)
def show_vacancy(company_id: int = Path(
    ...,
    ge=1,
    title="Company ID",
    description="This is the company ID",
    example= 1
    )):
    with open("empresas.json", 'r', encoding="utf-8") as f:
        results = json.loads(f.read())
        id = company_id
    for data in results:
        if data["company_id"] == id:
            return data
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"¡This company_id doesn't exist!"
        )


