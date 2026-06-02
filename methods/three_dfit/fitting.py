# methods/three_dfit/fitting.py

import numpy as np

from scipy.optimize import minimize


def fit_group_implicit(group):

    data = group["data"]

    x_raw = data["x"]
    y_raw = data["y"]
    t_raw = data["t"]

    # -----------------------------
    # Centering
    # -----------------------------
    x_m = np.mean(x_raw)
    y_m = np.mean(y_raw)

    t_0 = t_raw.min()

    x = x_raw - x_m
    y = y_raw - y_m
    t = t_raw - t_0

    # -----------------------------
    # Initial frequency estimate
    # -----------------------------
    y_c = y - np.mean(y)

    freqs = np.linspace(
        1,
        300,
        200
    )

    power = [
        np.abs(
            np.sum(
                y_c *
                np.exp(
                    -1j *
                    2 *
                    np.pi *
                    f *
                    t
                )
            )
        )
        for f in freqs
    ]

    f_init = freqs[
        np.argmax(power)
    ]

    # -----------------------------
    # Initial parameters
    # -----------------------------
    p0 = [
        0.0,
        1.0,
        np.ptp(y) / 2,
        f_init,
        0.0,
        0.1,
        0.0
    ]

    # -----------------------------
    # Objective
    # -----------------------------
    def objective(p):

        A, B, C, f, phi, lamb, D = p

        penalty = (
            1e6 *
            (
                np.sqrt(
                    A**2 + B**2
                ) - 1
            )**2
        )

        vibration = (
            C *
            np.exp(-lamb * t) *
            np.sin(
                2 *
                np.pi *
                f *
                t +
                phi
            )
        )

        residual = (
            A * x +
            B * y +
            vibration +
            D
        )

        return (
            np.mean(
                residual**2
            )
            +
            penalty
        )

    bounds = [
        (-1, 1),
        (-1, 1),
        (0, None),
        (1, 500),
        (-np.pi, np.pi),
        (0, 10),
        (None, None)
    ]

    result = minimize(
        objective,
        p0,
        method="L-BFGS-B",
        bounds=bounds
    )

    if not result.success:
        return None

    popt = result.x

    norm = np.sqrt(
        popt[0]**2 +
        popt[1]**2
    )

    popt[[0, 1, 2, 6]] /= norm

    return {
        "params": popt,
        "x_m": x_m,
        "y_m": y_m,
        "t_0": t_0,
        "id": group["id"],
        "x_range": group["x_range"]
    }
