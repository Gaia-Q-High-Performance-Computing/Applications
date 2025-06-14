import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from core.route_optimizer import optimize_route


def test_optimize_route_placeholder():
    assert optimize_route({}) == {}
