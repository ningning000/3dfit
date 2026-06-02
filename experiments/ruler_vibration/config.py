from dataclasses import dataclass


@dataclass
class RulerConfig:

    file_path: str

    roi_x_min: int
    roi_x_max: int

    roi_y_min: int
    roi_y_max: int

    t_min: float
    t_max: float
