import numpy as np


def frequency_error(gt, pred):
    return abs(pred - gt)


def frequency_relative_error(gt, pred):
    return abs(pred - gt) / gt * 100


def amplitude_error(gt, pred):
    return abs(pred - gt)


def rmse(gt_values, pred_values):

    gt_values = np.asarray(gt_values)
    pred_values = np.asarray(pred_values)

    return np.sqrt(
        np.mean(
            (gt_values - pred_values) ** 2
        )
    )
