from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - fallback for restricted envs
    yaml = None


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
        text = f.read()

    if yaml is not None:
        data = yaml.safe_load(text)
        summary = data.get("description", {}).get("summary", "")
    else:
        data = _simple_yaml_load(text)
        summary = _extract_description_summary(text)

    return AgentProfile(
        agent_id=data.get("agent_id", ""),
        agent_name=data.get("agent_name", ""),
        description=summary,
        metadata=data.get("metadata", {}),
    )


def load_cfd_automation_config(path: Path) -> Dict[str, Any]:
    """Load the GAIA-QAO CFD Automation Script configuration from a YAML file."""
    with path.open("r", encoding="utf-8") as f:
        text = f.read()

    if yaml is not None:
        return yaml.safe_load(text)
    return _simple_yaml_load(text)


def _simple_yaml_load(text: str) -> Dict[str, Any]:
    """Very small YAML subset parser used if PyYAML is unavailable."""
    data: Dict[str, Any] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            val = value.strip().strip('"')
            data[key.strip()] = val
    return data


def _extract_description_summary(text: str) -> str:
    """Extract the description.summary field using regex."""
    import re

    match = re.search(r"^description:\n\s*summary:\s*\"?(.*?)\"?$", text, re.MULTILINE)
    return match.group(1).strip('"') if match else ""
