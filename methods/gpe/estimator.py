# methods/gpe/estimator.py

from methods.base import BaseEstimator

from .frame_builder import (
    events_to_frames
)

from .phase import (
    phase_vibration_analysis
)


class GPE(BaseEstimator):

    def __init__(
        self,
        frame_dt=0.002,
        min_events=50
    ):

        self.frame_dt = frame_dt
        self.min_events = min_events

    def estimate(
        self,
        roi
    ):

        frames, times = (
            events_to_frames(
                roi,
                frame_dt=self.frame_dt,
                min_events=self.min_events
            )
        )

        if len(frames) < 2:

            return {
                "frequency": None,
                "success": False
            }

        result = (
            phase_vibration_analysis(
                frames,
                times
            )
        )

        return {
            "frequency":
                result["frequency"],

            "signal":
                result["signal"],

            "freqs":
                result["freqs"],

            "spectrum":
                result["spectrum"],

            "times":
                times,

            "success":
                True
        }
