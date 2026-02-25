#!/usr/bin/env python3
"""
ex0 - space_station.py
Pydantic v2 basic model + Field validation.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Represents a space station with validated attributes."""

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)

    crew_size: int = Field(..., ge=1, le=20)

    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)

    last_maintenance: datetime

    is_operational: bool = True

    notes: Optional[str] = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:
    """Display station information."""
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")

    status = "Operational" if station.is_operational else "Offline"
    print(f"Status: {status}")


def clean_error_message(exc: ValidationError) -> str:
    """Return clean validation message."""
    msg = exc.errors()[0]["msg"]
    prefix = "Value error, "

    if msg.startswith(prefix):
        msg = msg[len(prefix):]

    return msg


def main() -> None:
    """Demonstration function."""

    print("Space Station Data Validation")
    print("=" * 40)

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T10:30:00",
        )

        display_station(station)

    except ValidationError as exc:
        print("Validation error:")
        print(clean_error_message(exc))

    print("=" * 40)

    try:
        SpaceStation(
            station_id="ISS002",
            name="Deep Space Relay",
            crew_size=25,
            power_level=70.0,
            oxygen_level=80.0,
            last_maintenance="2024-02-01T08:00:00",
        )

    except ValidationError as exc:
        print("Expected validation error:")
        print(clean_error_message(exc))


if __name__ == "__main__":
    main()
