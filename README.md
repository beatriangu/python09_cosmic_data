🪐 Cosmic Data — Declarative Data Modeling with Pydantic v2

Designing self-validating data contracts using modern Python typing and Pydantic v2.

This project explores how structured models enforce integrity
at the moment of instantiation — not through scattered defensive checks.

🎯 Core Objective

Shift from procedural validation:

if value < 0:
    raise ValueError

to declarative schema-driven modeling:

value: int = Field(ge=0)

The model becomes the single source of truth.

## 🗺️ Conceptual Map

```text
                ┌────────────────────┐
                │     BaseModel      │
                └─────────┬──────────┘
                          │
            ┌─────────────┴─────────────┐
            │                           │
     Field Validation            Model Validation
     (local rules)              (relational rules)
            │                           │
   • Length constraints          • Cross-field logic
   • Numeric bounds              • Business coherence
   • Regex patterns              • System integrity
            │                           │
            └─────────────┬─────────────┘
                          │
                  Nested Models
                          │
                 Structural Consistency


📂 Exercise Progression
🔹 ex0 — SpaceStation

Field-level declarative validation.

🔹 ex1 — AlienContact

Cross-field business rules via @model_validator.

🔹 ex2 — SpaceCrew

Nested models + system-level safety constraints.

Each step increases structural depth.

🏗 Architectural Evolution
Manual checks  →  Declarative constraints  →  Executable schema
Flow control   →  Model-centric validation →  Structural guarantees

Validation moves:

From scattered logic
To centralized contracts.

🔎 What This Demonstrates

Well-designed data models:

Enforce integrity by construction

Reduce duplicated validation logic

Improve traceability of errors

Scale from simple fields to complex systems

📌 Key Insight

The model is not a container.

It is an executable contract.

Structure is stronger than control flow.