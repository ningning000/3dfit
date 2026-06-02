# experiments/simulation/simulator.py

import numpy as np


def y_vibration(t, cfg):

    return (
        cfg.rod_y_center
        +
        cfg.amplitude
        *
        np.sin(
            2 * np.pi * cfg.freq * t
            + cfg.phase
        )
    )


def generate_rod_events(cfg):

    t_list = np.arange(
        0,
        cfg.t_total,
        cfg.t_resolution
    )

    x_coords = np.arange(
        cfg.rod_x_start,
        cfg.rod_x_start + cfg.rod_length
    )

    y_base = np.arange(
        cfg.rod_y_center - cfg.rod_width // 2,
        cfg.rod_y_center + cfg.rod_width // 2
    )

    X, Yb = np.meshgrid(
        x_coords,
        y_base
    )

    num_pixels = X.size

    x_e = []
    y_e = []
    t_e = []
    p_e = []

    for t in t_list:

        y_cur = y_vibration(
            t,
            cfg
        )

        Y = (
            Yb
            +
            (
                y_cur
                -
                cfg.rod_y_center
            )
        )

        Y += np.random.normal(
            0,
            cfg.noise_level
            *
            cfg.amplitude,
            Y.shape
        )

        n = int(
            cfg.event_density
            *
            cfg.t_resolution
            *
            num_pixels
        )

        if n <= 0:
            continue

        idx = np.random.choice(
            num_pixels,
            n,
            replace=True
        )

        x_e.append(
            X.flatten()[idx]
        )

        y_e.append(
            Y.flatten()[idx]
        )

        t_e.append(
            np.full(n, t)
        )

        p_e.append(
            np.random.choice(
                [-1, 1],
                n
            )
        )

    x = np.concatenate(x_e)
    y = np.concatenate(y_e)
    t = np.concatenate(t_e)
    p = np.concatenate(p_e)

    t += np.random.normal(
        0,
        cfg.temporal_jitter,
        len(t)
    )

    n_bg = int(
        len(t)
        *
        cfg.background_ratio
    )

    x_bg = np.random.uniform(
        x.min(),
        x.max(),
        n_bg
    )

    y_bg = np.random.uniform(
        y.min(),
        y.max(),
        n_bg
    )

    t_bg = np.random.uniform(
        t.min(),
        t.max(),
        n_bg
    )

    p_bg = np.random.choice(
        [-1, 1],
        n_bg
    )

    x = np.concatenate(
        [x, x_bg]
    )

    y = np.concatenate(
        [y, y_bg]
    )

    t = np.concatenate(
        [t, t_bg]
    )

    p = np.concatenate(
        [p, p_bg]
    )

    return {
        "x": x,
        "y": y,
        "t": t,
        "p": p
    }
