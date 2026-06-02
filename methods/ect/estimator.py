# methods/ect/estimator.py

from methods.base import BaseEstimator

from .centroid import (
    event_centroid_tracking
)

from .frequency import (
    phase_with_fft
)


class ECT(BaseEstimator):

    def __init__(
        self,
        dt=0.001,
        min_events=30,
        smooth_sigma=1.0
    ):

        self.dt = dt
        self.min_events = min_events
        self.smooth_sigma = smooth_sigma

    def estimate(
        self,
        roi
    ):

        times, centers = (
            event_centroid_tracking(
                roi,
                dt=self.dt,
                min_events=self.min_events,
                smooth_sigma=self.smooth_sigma
            )
        )

        result = phase_with_fft(
            times,
            centers
        )

        amplitude = (
            0.5 *
            (
                result["signal"].max()
                -
                result["signal"].min()
            )
        )

        return {
            "frequency":
                result["fft_frequency"],

            "phase_frequency":
                result["phase_frequency"],

            "amplitude":
                amplitude,

            "signal":
                result["signal"],

            "times":
                times,

            "freqs":
                result["freqs"],

            "spectrum":
                result["spectrum"],

            "success":
                True
        }
