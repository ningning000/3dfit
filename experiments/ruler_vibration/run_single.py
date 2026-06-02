from datasets.loader import load_events
from datasets.roi import select_roi

from methods.three_dfit.three_dfit import ThreeDFIT
from methods.ect.ect import ECT
from methods.gpe.gpe import GPE


def run_single(config):

    data = load_events(
        config.file_path
    )

    roi = select_roi(
        data,
        config.roi_x_min,
        config.roi_x_max,
        config.roi_y_min,
        config.roi_y_max,
        config.t_min,
        config.t_max
    )

    methods = {
        "3DFIT": ThreeDFIT(),
        "ECT": ECT(),
        "GPE": GPE()
    }

    results = {}

    for name, method in methods.items():

        results[name] = method.estimate(
            roi
        )

    return results
