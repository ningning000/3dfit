# experiments/simulation/evaluator.py


def frequency_error(
    gt,
    pred
):
    return abs(pred - gt)


def amplitude_error(
    gt,
    pred
):
    return abs(pred - gt)
