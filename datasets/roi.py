# datasets/roi.py

import numpy as np


def select_roi(
    events,
    x_min,
    x_max,
    y_min,
    y_max,
    t_min,
    t_max
):
    """
    Spatial-temporal ROI selection.

    Parameters
    ----------
    events : dict

    x_min, x_max : float
    y_min, y_max : float
    t_min, t_max : float

    Returns
    -------
    roi : dict
    """

    mask = (
        (events["x"] >= x_min)
        & (events["x"] <= x_max)
        & (events["y"] >= y_min)
        & (events["y"] <= y_max)
        & (events["t"] >= t_min)
        & (events["t"] <= t_max)
    )

    roi = {}

    for key, value in events.items():

        if value is None:
            roi[key] = None
        else:
            roi[key] = value[mask]

    return roi
