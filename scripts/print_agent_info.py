#!/usr/bin/env python3
"""Utility script to display basic agent information."""
import argparse
from pathlib import Path

from gaia_qao.agent import load_agent_profile


def main() -> None:
    parser = argparse.ArgumentParser(description="Display agent profile info")
    parser.add_argument(
        "profile",
        type=Path,
        default=Path("Q-AI/agent_profile_sustainability.yaml"),
        nargs="?",
        help="Path to agent profile YAML",
    )
    args = parser.parse_args()

    profile = load_agent_profile(args.profile)
    print(f"Agent ID: {profile.agent_id}")
    print(f"Agent Name: {profile.agent_name}")
    print(f"Description: {profile.description}")


if __name__ == "__main__":
    main()
