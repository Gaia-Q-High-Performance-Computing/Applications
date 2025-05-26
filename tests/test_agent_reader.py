from pathlib import Path

from gaia_qao.agent import load_agent_profile, load_cfd_automation_config


def test_load_agent_profile():
    profile = load_agent_profile(Path("Q-AI/agent_profile_sustainability.yaml"))
    assert profile.agent_id == "agent-env-sustainability-001"
    assert profile.agent_name == "Environmental Sustainability Specialist"


def test_load_cfd_automation_config():
    config = load_cfd_automation_config(Path("scripts/runCFD.sh"))
    assert "DEFAULT_CORES" in config
    assert "LOG_DIR" in config
    assert "CASE_DIR" in config
