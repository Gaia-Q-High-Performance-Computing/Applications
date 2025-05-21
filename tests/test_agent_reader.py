from pathlib import Path

from gaia_qao.agent import load_agent_profile


def test_load_agent_profile():
    profile = load_agent_profile(Path("Q-AI/agent_profile_sustainability.yaml"))
    assert profile.agent_id == "agent-env-sustainability-001"
    assert profile.agent_name == "Environmental Sustainability Specialist"
