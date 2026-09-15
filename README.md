# Learn Pydantic

> Learn Pydantic v2 by example — validators, nested models & serialization with 6 hands-on demos

A beginner-friendly Pydantic v2 crash course with 6 practical examples: `BaseModel` & `Field` validation, `field_validator`, `model_validator`, `computed_field`, nested models and `model_dump` serialization. Built with Patient model examples.

## What is Pydantic?

Pydantic is a Python library for **data validation, data parsing, and data management using Python type hints**. You define the structure and expected data types of your data using Python classes inheriting from `BaseModel`. Pydantic validates at runtime, coerces types when possible, and gives clear errors.

Useful when data comes from outside sources: **API requests, JSON, Forms, Config files, Databases**, etc.

## Why Pydantic?

- Runtime validation with Python type hints (fail fast)
- Automatic type coercion + strict mode (`strict=True`)
- Rich built-in types: `EmailStr`, `AnyUrl` and constrained `Field`
- Custom business logic via `field_validator` / `model_validator`
- Derived values via `computed_field` without storing them
- Hierarchical data via nested `BaseModel`s
- Serialization with `model_dump()` / `model_dump_json()`

## Project Structure

| File | Concept | Key APIs |
|------|---------|----------|
| `1_why_pydantic.py` | Why Pydantic & Basic Field Validation | `BaseModel`, `Field`, `Annotated`, `EmailStr`, `AnyUrl` |
| `2_field_validator.py` | Field-level Custom Validation | `@field_validator`, `mode='after'` |
| `3_model_validator.py` | Cross-field / Model-level Validation | `@model_validator(mode='after')` |
| `4_computed_fields.py` | Derived Fields | `@computed_field` + `@property` |
| `5_nested_models.py` | Hierarchical / Nested Models | Nested `BaseModel`, `model_dump()` |
| `6_serialization.py` | Serialization & Export | `model_dump(exclude_unset=True)` |

## Concepts Covered

### 1. Why Pydantic & Field Validation — `1_why_pydantic.py:10`
- `Annotated[str, Field(max_length=50, title, description, examples)]` for docs & constraints
- `EmailStr`, `AnyUrl` for format validation
- `Field(gt=0, lt=120)` for range, `Annotated[float, Field(gt=0, strict=True)]` for strict type checking
- `Annotated[Optional[List[str]], Field(default=None, max_length=5)]` for optional + nested validation
- `Dict[str, str]` for free-form contact details

### 2. Field Validator — `2_field_validator.py:17`
```python
@field_validator('email')
@classmethod
def email_validator(cls, value):
    domain = value.split('@')[-1]
    if domain not in ['hdfc.com', 'icici.com']:
        raise ValueError('Not a valid domain')
    return value

@field_validator('name')
@classmethod
def transform_name(cls, value):
    return value.upper()  # transform

@field_validator('age', mode='after')
@classmethod
def validate_age(cls, value):
    if 0 < value < 100: return value
    raise ValueError('Age should be in between 0 and 100')
```
- `mode='before'` (default) vs `mode='after'` (after type coercion)

### 3. Model Validator — `3_model_validator.py:18`
```python
@model_validator(mode='after')
def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
        raise ValueError('Patients older than 60 must have an emergency contact')
    return model
```
- Validates relationships between multiple fields.

### 4. Computed Fields — `4_computed_fields.py:18`
```python
@computed_field
@property
def bmi(self) -> float:
    return round(self.weight/(self.height**2), 2)
```
- Value derived from `weight` (kg) and `height` (m), not required as input, included in `model_dump()`.

### 5. Nested Models — `5_nested_models.py:6`
```python
class Address(BaseModel):
    city: str; state: str; pin: str

class Patient(BaseModel):
    name: str; gender: str; age: int; address: Address

address1 = Address(**address_dict)
patient1 = Patient(name='nitish', age=35, address=address1)
patient1.model_dump()
```
- Benefits: organization, reusability (`Address` in multiple models), readability, automatic nested validation.

### 6. Serialization — `6_serialization.py:24`
```python
patient1.model_dump(exclude_unset=True)  # only fields explicitly set
patient1.model_dump_json()               # JSON string
```
- `model_dump()` vs `model_dump(include=...)` / `exclude_unset=True` / `exclude_defaults=True`

## Installation

Requires Python >= 3.13 (tested on 3.13.9). Dependencies are defined in `pyproject.toml`.

```bash
# with pip
pip install -e .

# or directly
pip install "pydantic[email]>=2.0" email-validator typing_extensions
```

No install is needed just to browse the examples — Pydantic is required only to run them.

## Usage

```bash
python 1_why_pydantic.py
python 2_field_validator.py
python 3_model_validator.py
python 4_computed_fields.py
python 5_nested_models.py
python 6_serialization.py
```

Example — `1_why_pydantic.py:31`:
```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    email: EmailStr
    age: int = Field(gt=0, lt=120)

patient_info = {'name':'sonu', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}
patient1 = Patient(**patient_info)
```

## Requirements

See `pyproject.toml` for full dependency list.

- `pydantic[email] >= 2.0`
- `email-validator` (for `EmailStr`)
- `typing_extensions` (for `Annotated` on Python < 3.9)

## Author

Sudhansu — [github.com/Sudhansu490](https://github.com/Sudhansu490)
