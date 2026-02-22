# 🪐 Cosmic Data — Data Modeling with Pydantic v2

A structured approach to **data validation and modeling** using  
**Pydantic v2** and modern Python type hints.

This project explores how to design models that:

- Validate themselves at instantiation time
- Enforce structural integrity
- Centralize business rules
- Reduce defensive boilerplate code
- Scale from simple validation to system-level coherence

---

## 🎯 Project Goal

Move from manual validation logic:

```python
if value < 0:
    raise ValueError(...)

to declarative, schema-driven models:

value: int = Field(ge=0)

The objective is not just to validate data,
but to design self-contained, self-validating structures.

🧠 Concepts Practiced

BaseModel

Type hints as data contracts

Field() constraints

Length validation

Numeric bounds

Regular expressions

Enum for controlled values

@model_validator(mode="after")

Nested models

Cross-field validation

Structured error handling with ValidationError

📂 Exercises
ex0 — SpaceStation

Basic field-level validation:

String length constraints

Regex-based validation

Numeric range enforcement

Focus: declarative validation at attribute level.

ex1 — AlienContact

Introduces business logic rules using:

Enum

Cross-field validation

model_validator

Focus: enforcing relational rules between attributes.

ex2 — SpaceCrew

Nested models and aggregated validation:

CrewMember inside SpaceMission

Leadership requirements

Experience distribution constraints

Global mission-level coherence

Focus: validating system integrity, not just individual fields.

🚀 How to Run

Create a virtual environment and install dependencies:

python3 -m venv .venv
source .venv/bin/activate
pip install "pydantic>=2,<3"

Run each exercise individually:

python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py

Each script demonstrates:

A valid instance

An invalid instance

Structured validation errors

🏗️ Architectural Insight

This project demonstrates a shift from:

Procedural validation
→ Declarative structural design

The models act as executable schemas that guarantee consistency
by construction.

Instead of validating data everywhere,
validation becomes part of the model definition itself.

📌 Key Takeaway

Well-designed data models:

Reduce duplication

Increase clarity

Prevent invalid states

Improve maintainability

Structure is stronger than control flow.