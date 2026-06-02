# methods/ect/centroid.py

import numpy as np

from scipy.ndimage import gaussian_filter1d


def event_centroid_tracking(
    events,
    dt=0.001,
    min_events=30,
    smooth_sigma=1.0
):
    """
    Event Centroid Tracking (ECT)

    Parameters
    ----------
    events : dict
    dt : float
        Time bin width (s)
    min_events : int
    smooth_sigma : float

    Returns
    -------
    times : ndarray
    centers : ndarray
    """

    t = events["t"]
    y = events["y"]

    t0 = t.min()
    t1 = t.max()

    centers = []
    times = []

    n_bins = int(
        (t1 - t0) // dt
    )

    for i in range(n_bins):

        ta = t0 + i * dt
        tb = ta + dt

        mask = (
            (t >= ta)
            &
            (t < tb)
        )

        if np.sum(mask) < min_events:
            continue

        yc = np.mean(
            y[mask]
        )

        centers.append(yc)

        times.append(
            (ta + tb) / 2
        )

    centers = np.array(
        centers
    )

    times = np.array(
        times
    )

    # remove DC
    centers = (
        centers
        -
        np.mean(centers)
    )

    # smoothing
    centers = gaussian_filter1d(
        centers,
        sigma=smooth_sigma
    )

    return times, centers
