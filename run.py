# run.py

import argparse
import yaml
import json
import numpy as np

from pathlib import Path

from datasets.loader import load_events
from datasets.roi import select_roi

from methods.three_dfit import ThreeDFIT
from methods.ect import ECT
from methods.gpe import GPE

from metrics import (
    frequency_error,
    frequency_relative_error,
    amplitude_error,
    amplitude_relative_error
)


# =========================================================
# Method Registry
# =========================================================

METHODS = {
    "3dfit": ThreeDFIT,
    "ect": ECT,
    "gpe": GPE
}


# =========================================================
# JSON Converter
# =========================================================

def convert_numpy(obj):

    if isinstance(obj, np.ndarray):
        return obj.tolist()

    if isinstance(obj, np.floating):
        return float(obj)

    if isinstance(obj, np.integer):
        return int(obj)

    raise TypeError(
        f"Object of type {type(obj)} "
        f"is not JSON serializable"
    )


# =========================================================
# Load Config
# =========================================================

def load_config(config_path):

    with open(config_path, "r") as f:
        cfg = yaml.safe_load(f)

    return cfg


# =========================================================
# Build Method
# =========================================================

def build_method(method_name):

    method_name = method_name.lower()

    if method_name not in METHODS:

        raise ValueError(
            f"Unknown method: {method_name}"
        )

    return METHODS[method_name]()


# =========================================================
# Run Experiment
# =========================================================

def run_experiment(method_name, config_path):

    cfg = load_config(config_path)

    print("\nLoading dataset...")

    data = load_events(
        cfg["dataset"]
    )

    roi_cfg = cfg["roi"]
    time_cfg = cfg["time"]

    roi_data = select_roi(
        data,
        roi_cfg["x_min"],
        roi_cfg["x_max"],
        roi_cfg["y_min"],
        roi_cfg["y_max"],
        time_cfg["start"],
        time_cfg["end"]
    )

    print(
        f"ROI Events: {len(roi_data['x'])}"
    )

    # -----------------------------------------------------
    # Build Method
    # -----------------------------------------------------

    method = build_method(
        method_name
    )

    print(
        f"Running {method_name.upper()}..."
    )

    result = method.estimate(
        roi_data
    )

    # -----------------------------------------------------
    # Check Success
    # -----------------------------------------------------

    if not result.get("success", False):

        print(
            "\nEstimation failed."
        )

        return result

    # -----------------------------------------------------
    # Print Result
    # -----------------------------------------------------

    print("\nResult:")

    if result.get("frequency") is not None:

        print(
            f"Frequency = "
            f"{result['frequency']:.3f} Hz"
        )

    if result.get("amplitude") is not None:

        print(
            f"Amplitude = "
            f"{result['amplitude']:.3f}"
        )

    # -----------------------------------------------------
    # Metrics
    # -----------------------------------------------------

    if "ground_truth" in cfg:

        gt = cfg["ground_truth"]

        print("\nMetrics")

        # --------------------------
        # Frequency
        # --------------------------

        if result.get("frequency") is not None:

            freq_err = frequency_error(
                gt["frequency"],
                result["frequency"]
            )

            freq_rel = frequency_relative_error(
                gt["frequency"],
                result["frequency"]
            )

            print(
                f"Frequency Error: "
                f"{freq_err:.4f} Hz"
            )

            print(
                f"Frequency Relative Error: "
                f"{freq_rel:.2f}%"
            )

            result["frequency_error"] = float(
                freq_err
            )

            result["frequency_relative_error"] = float(
                freq_rel
            )

        # --------------------------
        # Amplitude
        # --------------------------

        if (
            "amplitude" in gt
            and
            result.get("amplitude") is not None
        ):

            amp_err = amplitude_error(
                gt["amplitude"],
                result["amplitude"]
            )

            amp_rel = amplitude_relative_error(
                gt["amplitude"],
                result["amplitude"]
            )

            print(
                f"Amplitude Error: "
                f"{amp_err:.4f}"
            )

            print(
                f"Amplitude Relative Error: "
                f"{amp_rel:.2f}%"
            )

            result["amplitude_error"] = float(
                amp_err
            )

            result["amplitude_relative_error"] = float(
                amp_rel
            )

    return result


# =========================================================
# Save Result
# =========================================================

def save_result(
    result,
    method_name,
    config_path
):

    config_name = Path(
        config_path
    ).stem

    save_dir = (
        Path("results")
        / config_name
    )

    save_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    save_file = (
        save_dir
        / f"{method_name}.json"
    )

    with open(save_file, "w") as f:

        json.dump(
            result,
            f,
            indent=4,
            default=convert_numpy
        )

    print(
        f"\nSaved to: {save_file}"
    )


# =========================================================
# Main
# =========================================================

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--method",
        required=True,
        choices=[
            "3dfit",
            "ect",
            "gpe"
        ]
    )

    parser.add_argument(
        "--config",
        required=True
    )

    args = parser.parse_args()

    result = run_experiment(
        args.method,
        args.config
    )

    save_result(
        result,
        args.method,
        args.config
    )


# =========================================================
# Entry
# =========================================================

if __name__ == "__main__":
    main()
