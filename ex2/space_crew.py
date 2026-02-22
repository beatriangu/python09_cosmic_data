#!/usr/bin/env python3
"""
ex2 - space_crew.py
Pydantic v2 nested models + mission-level validation.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Crew member ranks."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Represents a crew member in a space mission."""

    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    years_experience: int = Field(..., ge=0)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Represents a space mission with a crew roster."""

    mission_id: str = Field(..., pattern=r"^M.*")
    duration_days: int = Field(..., gt=0)
    crew: list[CrewMember] = Field(..., min_length=1)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Validate mission-level rules that require multiple fields."""
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "mission_id must start with 'M'."
            )

        if any(not member.is_active for member in self.crew):
            raise ValueError(
                "All crew members must be active."
            )

        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must include at least one Commander or Captain."
            )

        if self.duration_days > 365:
            experienced = [
                member
                for member in self.crew
                if member.years_experience >= 5
            ]
            ratio = len(experienced) / len(self.crew)
            if ratio < 0.5:
                raise ValueError(
                    "Long missions (>365 days) require at least 50% "
                    "of crew members with 5+ years of experience."
                )

        return self


def main() -> None:
    try:
        mission = SpaceMission(
            mission_id="M-42",
            duration_days=400,
            crew=[
                CrewMember(
                    name="Astra Nova",
                    rank=Rank.COMMANDER,
                    years_experience=12,
                    is_active=True,
                ),
                CrewMember(
                    name="Orion Pike",
                    rank=Rank.OFFICER,
                    years_experience=6,
                    is_active=True,
                ),
                CrewMember(
                    name="Lyra Kade",
                    rank=Rank.LIEUTENANT,
                    years_experience=2,
                    is_active=True,
                ),
                CrewMember(
                    name="Milo Rook",
                    rank=Rank.CADET,
                    years_experience=0,
                    is_active=True,
                ),
            ],
        )
        print("Valid:")
        print(mission)
    except ValidationError as exc:
        print("Validation error:")
        print(exc)

    print("-" * 40)

    try:
        invalid_mission = SpaceMission(
            mission_id="M-99",
            duration_days=500,
            crew=[
                CrewMember(
                    name="No Leader",
                    rank=Rank.OFFICER,
                    years_experience=1,
                    is_active=True,
                ),
                CrewMember(
                    name="Short Exp",
                    rank=Rank.LIEUTENANT,
                    years_experience=2,
                    is_active=True,
                ),
            ],
        )
        print("Valid:")
        print(invalid_mission)
    except ValidationError as exc:
        print("Validation error:")
        print(exc)


if __name__ == "__main__":
    main()
