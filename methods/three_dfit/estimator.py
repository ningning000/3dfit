# methods/three_dfit/estimator.py

import numpy as np

from methods.base import BaseEstimator

from .grouping import group_by_x
from .fitting import fit_group_implicit


class ThreeDFIT(BaseEstimator):

    def __init__(
        self,
        group_size=800,
        min_events=100
    ):

        self.group_size = group_size
        self.min_events = min_events

    def estimate(self, roi):

        groups = group_by_x(
            roi,
            group_size=self.group_size,
            min_events=self.min_events
        )

        fitted_groups = []

        for group in groups:

            result = fit_group_implicit(
                group
            )

            if result is not None:
                fitted_groups.append(
                    result
                )

        if len(fitted_groups) == 0:

            return {
                "frequency": None,
                "success": False
            }

        frequencies = [
            g["params"][3]
            for g in fitted_groups
        ]

        frequency = np.median(
            frequencies
        )

        return {
            "frequency": float(frequency),
            "amplitude": None,
            "success": True
        }
