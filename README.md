# Learn Pydantic

> Learn Pydantic v2 by example — 6 simple hands-on demos.

A beginner-friendly crash course covering Pydantic v2 with Patient model examples.

## What is Pydantic?

A Python library for **data validation and parsing using type hints**. Define your data shape with a `BaseModel` class — Pydantic validates and gives clear errors at runtime.

Useful for: API requests, JSON, Forms, Config files, Databases.

## Why Pydantic?

- Validates data automatically using type hints
- Built-in types like `EmailStr`, `AnyUrl`
- Add constraints with `Field` (e.g. `gt`, `max_length`)
- Custom rules with validators
- Handles nested data and serialization

## Project Structure

| File | What You Learn |
|------|----------------|
| `1_why_pydantic.py` | Basics — `BaseModel`, `Field`, `EmailStr`, `AnyUrl` |
| `2_field_validator.py` | Custom validation for a single field |
| `3_model_validator.py` | Validation using multiple fields |
| `4_computed_fields.py` | Auto-calculated fields (e.g. BMI) |
| `5_nested_models.py` | Models inside models (Address → Patient) |
| `6_serialization.py` | Convert models to dict/JSON |

## Concepts in Brief

1. **Field Validation** — Set rules like email format, age range, strict types.
2. **Field Validator** — Custom logic for one field (e.g. allow only certain email domains).
3. **Model Validator** — Rule that checks multiple fields together (e.g. emergency contact if age > 60).
4. **Computed Field** — Value calculated from other fields (e.g. `bmi = weight / height²`).
5. **Nested Models** — Keep related data organized and validated.
6. **Serialization** — Export model to `dict` or `JSON` with `model_dump()`.

## Installation

Requires **Python >= 3.13** (tested on 3.13.9).

```bash
pip install -e .
```

Or directly:
```bash
pip install "pydantic[email]>=2.0"
```

## Usage

```bash
python 1_why_pydantic.py
python 2_field_validator.py
python 3_model_validator.py
python 4_computed_fields.py
python 5_nested_models.py
python 6_serialization.py
```

## Requirements

See `pyproject.toml`:

- `pydantic[email] >= 2.0`
- `email-validator`
- `typing_extensions`

## Author

Sudhansu — [github.com/Sudhansu490](https://github.com/Sudhansu490)
