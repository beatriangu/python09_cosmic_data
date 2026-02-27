🪐 Python Module — Cosmic Data
Declarative Modeling & Structural Validation with Pydantic v2
1️⃣ Module Purpose

Introduce structured data modeling through Pydantic v2, treating models as executable contracts.

Focus:

Declarative typed schemas

Centralized structural and business rules

Integrity at instantiation time

Separation from imperative validation logic

This marks the transition from defensive validation to architectural design.

2️⃣ Core Technical Concepts

BaseModel as structural backbone

Type hints as formal contracts

Field() for declarative constraints:

min_length / max_length

ge / le

pattern

Enum for closed domains

@model_validator(mode="after") for relational rules

Nested models

Structured error handling (ValidationError)

3️⃣ Exercise Progression
🔹 ex0 — SpaceStation

Field-level validation embedded directly in the model definition.

Key idea:
Basic validation belongs to the data schema, not the execution flow.

🔹 ex1 — AlienContact

Relational validation and business logic integration.

Introduces:

Domain restriction via Enum

Cross-field consistency rules

Conditional business constraints

Key idea:
Business rules live inside the model.

🔹 ex2 — SpaceCrew

Nested entities and system-wide structural integrity.

Includes:

Composite models (SpaceMission + CrewMember)

Aggregated safety rules

Global consistency checks

Key idea:
Validation can represent system integrity, not just field correctness.

4️⃣ Conceptual Shift

Before:

Dispersed validation

Repeated imperative checks

Execution-order dependency

After:

Centralized contracts

Model-driven guarantees

Integrity enforced at creation time

The model becomes an active structural boundary.

5️⃣ Architectural Value

Declarative modeling enables:

Reduced logic duplication

Explicit data contracts

Early error detection

Scalable structural design

System-wide coherence

Pydantic turns models into structural gateways that prevent inconsistent data from entering the system.

6️⃣ Closing Principle

Declare before checking.
Design before patching.
Model before executing.

Validation becomes design, not defense.