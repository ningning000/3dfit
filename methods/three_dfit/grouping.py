# methods/three_dfit/grouping.py

import numpy as np


def group_by_x(
    roi_data,
    group_size=200,
    min_events=100
):
    """
    Divide ROI into x-direction groups.
    """

    x_min = roi_data["x"].min()
    x_max = roi_data["x"].max()

    bounds = np.arange(
        x_min,
        x_max + group_size,
        group_size
    )

    groups = []

    for i in range(len(bounds) - 1):

        x0 = bounds[i]
        x1 = bounds[i + 1]

        mask = (
            (roi_data["x"] >= x0)
            &
            (roi_data["x"] < x1)
        )

        if np.sum(mask) < min_events:
            continue

        group_data = {}

        for k, v in roi_data.items():

            if v is None:
                continue

            group_data[k] = v[mask]

        groups.append(
            {
                "id": i,
                "x_range": (x0, x1),
                "data": group_data
            }
        )

    return groups
