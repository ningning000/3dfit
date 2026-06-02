# methods/ect/frequency.py

import numpy as np

from scipy.signal import hilbert


def phase_with_fft(
    times,
    signal
):
    """
    Frequency estimation using

    Hilbert phase
    +
    FFT
    """

    signal = (
        signal
        -
        np.mean(signal)
    )

    # -------------------------
    # Hilbert phase
    # -------------------------
    analytic = hilbert(
        signal
    )

    phase = np.unwrap(
        np.angle(analytic)
    )

    inst_freq = (
        np.diff(phase)
        /
        (
            2 *
            np.pi *
            np.diff(times)
        )
    )

    f_phase = np.median(
        inst_freq
    )

    # -------------------------
    # FFT
    # -------------------------
    fs = (
        1.0
        /
        np.mean(
            np.diff(times)
        )
    )

    N = len(signal)

    freqs = np.fft.rfftfreq(
        N,
        d=1/fs
    )

    spectrum = np.abs(
        np.fft.rfft(signal)
    )

    spectrum /= (
        spectrum.max()
        + 1e-12
    )

    idx = np.argmax(
        spectrum
    )

    f_fft = freqs[idx]

    return {
        "phase_frequency": f_phase,
        "fft_frequency": f_fft,
        "spectrum": spectrum,
        "freqs": freqs,
        "signal": signal
    }
