# methods/gpe/phase.py

import numpy as np

from .gabor import complex_gabor


def phase_vibration_analysis(
    frames,
    times
):
    """
    Gabor phase vibration analysis.
    """

    complex_stack = []

    for frame in frames:

        response = complex_gabor(
            frame,
            theta=np.pi / 2
        )

        complex_stack.append(
            response
        )

    complex_stack = np.array(
        complex_stack
    )

    phase = np.angle(
        complex_stack
    )

    amplitude = np.abs(
        complex_stack
    )

    phase_unwrap = np.unwrap(
        phase,
        axis=0
    )

    dphi = np.diff(
        phase_unwrap,
        axis=0
    )

    signal = (
        np.sum(
            dphi * amplitude[:-1],
            axis=(1, 2)
        )
        /
        (
            np.sum(
                amplitude[:-1],
                axis=(1, 2)
            )
            +
            1e-6
        )
    )

    signal = (
        signal
        -
        np.mean(signal)
    )

    dt = (
        times[1]
        -
        times[0]
    )

    fft_vals = np.fft.rfft(
        signal
    )

    freqs = np.fft.rfftfreq(
        len(signal),
        d=dt
    )

    spectrum = np.abs(
        fft_vals
    )

    f_est = freqs[
        np.argmax(
            spectrum
        )
    ]

    return {
        "frequency": f_est,
        "signal": signal,
        "freqs": freqs,
        "spectrum": spectrum
    }
