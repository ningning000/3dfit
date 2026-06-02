# experiments/simulation/__init__.py
from .config import SimulationConfig
from .simulator import generate_rod_events

__all__ = [
    "SimulationConfig",
    "generate_rod_events"
]
