#!/usr/bin/env python3
"""
ex1 - alien_contact.py
Pydantic v2 model + mission-level validation.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)


class ContactType(str, Enum):
    """Allowed contact report types."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Represents an alien contact report."""

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType

    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)

    message_received: Optional[str] = Field(
        default=None,
        max_length=500,
    )
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        """Validate cross-field business rules."""

        if not self.contact_id.startswith("AC"):
            raise ValueError(
                'Contact ID must start with "AC"'
            )

        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError(
                "Physical contact reports must be verified"
            )

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires "
                "at least 3 witnesses"
            )

        if self.signal_strength > 7.0:
            msg = (self.message_received or "").strip()
            if not msg:
                raise ValueError(
                    "Strong signals (> 7.0) "
                    "should include received messages"
                )

        return self


def display_contact(contact: AlienContact) -> None:
    """Print contact report in subject style."""

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")

    if contact.message_received is not None:
        print(
            f"Message: '{contact.message_received}'"
        )


def clean_error_message(exc: ValidationError) -> str:
    """Return clean validation message."""

    msg = exc.errors()[0]["msg"]
    prefix = "Value error, "

    if msg.startswith(prefix):
        msg = msg[len(prefix):]

    return msg


def main() -> None:
    """Demonstration function."""

    print("Alien Contact Log Validation")
    print("=" * 38)

    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-05-10T21:15:00",
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received=(
                "Greetings from Zeta Reticuli"
            ),
        )

        display_contact(valid)

    except ValidationError as exc:
        print("Validation error:")
        print(clean_error_message(exc))

    print("=" * 38)

    try:
        AlienContact(
            contact_id="AC_2024_999",
            timestamp="2024-05-10T22:00:00",
            location="Desert Outpost",
            contact_type=ContactType.telepathic,
            signal_strength=6.0,
            duration_minutes=10,
            witness_count=1,
        )

    except ValidationError as exc:
        print("Expected validation error:")
        print(clean_error_message(exc))


if __name__ == "__main__":
    main()
