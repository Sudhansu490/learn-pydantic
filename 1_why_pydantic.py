# Pydantic is a Python library used for data validation, data parsing, and data management using Python type hints.
# It allows us to define the structure and expected data types of our data using Python classes.

# Pydantic is useful when an application receives data from outside sources, such as: API requests, JSON data, Forms, Configuration files, Databases etc.

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
# typing_extensions is required for Annotated type hinting

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Patient Name', description='Patient name should less than 50 chars', examples=['Sonu', 'Amit'])]
    # metadata can be added to the field using Field() function, which can be used for documentation purpose
    email: EmailStr        # email validation
    linkedin_url: AnyUrl     # AnyUrl validation
    age: int = Field(gt=0, lt=120)       # custom validation, age should be in between 0 & 120
    weight: Annotated[float, Field(gt=0, strict=True)]   # weight should be greater than 0 and strict type checking
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]   # default value is None, so it is optional
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]    # 2 level validation
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'sonu', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)
