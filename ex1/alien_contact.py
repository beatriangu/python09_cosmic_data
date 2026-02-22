#!/usr/bin/env python3
"""
ex1 - alien_contact.py
Pydantic v2 model with Enums and business rules using model_validator.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Possible types of alien contact."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Represents an alien contact report with validation rules."""

    contact_id: str = Field(..., pattern=r"^AC.*")
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    message_received: str | None = Field(default=None)
    witness_count: int = Field(..., ge=0)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        """Validate cross-field business rules."""
        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError(
                "Physical contact must be verified."
            )

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses."
            )

        if (
            self.signal_strength > 7.0
            and not self.message_received
        ):
            raise ValueError(
                "A message must be received when "
                "signal strength is above 7.0."
            )

        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "contact_id must start with 'AC'."
            )

        return self


def main() -> None:
    try:
        contact = AlienContact(
            contact_id="AC-2025-001",
            contact_type=ContactType.RADIO,
            signal_strength=8.2,
            message_received="We come in peace.",
            witness_count=1,
            is_verified=False,
        )
        print("Valid:")
        print(contact)
    except ValidationError as exc:
        print("Validation error:")
        print(exc)

    print("-" * 40)

    try:
        invalid_contact = AlienContact(
            contact_id="AC-2025-002",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=6.5,
            message_received=None,
            witness_count=2,
            is_verified=False,
        )
        print("Valid:")
        print(invalid_contact)
    except ValidationError as exc:
        print("Validation error:")
        print(exc)
