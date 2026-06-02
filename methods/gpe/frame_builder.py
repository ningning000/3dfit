# methods/gpe/frame_builder.py

import numpy as np
import cv2


def events_to_frames(
    events,
    frame_dt=0.001,
    min_events=50
):
    """
    Convert event stream to frame sequence.
    """

    xmin = int(events["x"].min())
    xmax = int(events["x"].max())

    ymin = int(events["y"].min())
    ymax = int(events["y"].max())

    W = xmax - xmin + 1
    H = ymax - ymin + 1

    t0 = events["t"].min()
    t1 = events["t"].max()

    frames = []
    times = []

    n_frames = int(
        (t1 - t0) / frame_dt
    )

    for k in range(n_frames):

        ta = t0 + k * frame_dt
        tb = ta + frame_dt

        mask = (
            (events["t"] >= ta)
            &
            (events["t"] < tb)
        )

        if np.sum(mask) < min_events:
            continue

        frame = np.zeros(
            (H, W),
            np.float32
        )

        xs = (
            events["x"][mask]
            - xmin
        ).astype(np.int32)

        ys = (
            events["y"][mask]
            - ymin
        ).astype(np.int32)

        for x, y in zip(xs, ys):
            frame[y, x] += 1.0

        frame = cv2.GaussianBlur(
            frame,
            (5, 5),
            0
        )

        frames.append(frame)

        times.append(
            (ta + tb) / 2
        )

    return (
        np.array(frames),
        np.array(times)
    )
