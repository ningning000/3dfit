# experiments/simulation/frequency_sweep.py

import pandas as pd

from .config import SimulationConfig
from .simulator import generate_rod_events

from methods.three_dfit import ThreeDFIT
from methods.ect import ECT
from methods.gpe import GPE


def run_frequency_sweep():

    frequencies = list(
        range(
            40,
            401,
            40
        )
    )

    three_dfit = ThreeDFIT()
    ect = ECT()
    gpe = GPE()

    results = []

    for freq in frequencies:

        cfg = SimulationConfig()
        cfg.freq = freq

        events = generate_rod_events(
            cfg
        )

        r1 = three_dfit.estimate(
            events
        )

        r2 = ect.estimate(
            events
        )

        r3 = gpe.estimate(
            events
        )

        results.append(
            {
                "gt_frequency": freq,

                "3dfit":
                    r1["frequency"],

                "ect":
                    r2["frequency"],

                "gpe":
                    r3["frequency"]
            }
        )

        print(
            f"Finished {freq} Hz"
        )

    df = pd.DataFrame(
        results
    )

    return df
