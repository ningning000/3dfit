# metrics/summary.py

import numpy as np


def mae(
    ground_truth,
    predictions
):
    """
    Mean Absolute Error
    """

    ground_truth = np.asarray(
        ground_truth
    )

    predictions = np.asarray(
        predictions
    )

    return np.mean(
        np.abs(
            predictions
            -
            ground_truth
        )
    )


def rmse(
    ground_truth,
    predictions
):
    """
    Root Mean Squared Error
    """

    ground_truth = np.asarray(
        ground_truth
    )

    predictions = np.asarray(
        predictions
    )

    return np.sqrt(
        np.mean(
            (
                predictions
                -
                ground_truth
            ) ** 2
        )
    )
