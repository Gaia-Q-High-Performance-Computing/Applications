from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

import yaml


@dataclass
class AgentProfile:
    """Simple representation of an agent profile."""

    agent_id: str
    agent_name: str
    description: str
    metadata: Dict[str, Any]


def load_agent_profile(path: Path) -> AgentProfile:
    """Load an agent profile from a YAML file."""
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return AgentProfile(
        agent_id=data.get("agent_id", ""),
        agent_name=data.get("agent_name", ""),
        description=data.get("description", {}).get("summary", ""),
        metadata=data.get("metadata", {}),
    )
