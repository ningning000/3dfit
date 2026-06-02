# experiments/simulation/config.py

from dataclasses import dataclass


@dataclass
class SimulationConfig:

    # vibration
    freq: float = 200.0
    amplitude: float = 10.0
    phase: float = 0.0

    # rod geometry
    rod_length: int = 400
    rod_width: int = 10

    rod_x_start: int = 200
    rod_y_center: int = 400

    # simulation time
    t_total: float = 0.1
    t_resolution: float = 2e-6

    # event density
    event_density: int = 2000

    # noise
    noise_level: float = 0.05
    background_ratio: float = 0.15
    temporal_jitter: float = 5e-6
