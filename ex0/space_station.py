#!/usr/bin/env python3
"""
ex0 - space_station.py
Pydantic v2 basic model + Field validation.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Represents a space station with validated attributes."""

    name: str = Field(..., min_length=3, max_length=50)
    location: str = Field(..., pattern=r".*Sector.*")
    crew_size: int = Field(..., ge=1, le=20)
    is_operational: bool


def main() -> None:
    try:
        station = SpaceStation(
            name="Orion Nexus",
            location="Sector 7G",
            crew_size=10,
            is_operational=True,
        )
        print("Valid:")
        print(station)
    except ValidationError as exc:
        print("Validation error:")
        print(exc)

    print("-" * 40)

    try:
        invalid_station = SpaceStation(
            name="OS",
            location="Unknown Zone",
            crew_size=25,
            is_operational=True,
        )
        print("Valid:")
        print(invalid_station)
    except ValidationError as exc:
        print("Validation error:")
        print(exc)
