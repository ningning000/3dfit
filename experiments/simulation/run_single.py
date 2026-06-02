# experiments/simulation/run_single.py

from .config import SimulationConfig
from .simulator import generate_rod_events

from methods.three_dfit import ThreeDFIT
from methods.ect import ECT
from methods.gpe import GPE


def main():

    cfg = SimulationConfig()

    events = generate_rod_events(
        cfg
    )

    three_dfit = ThreeDFIT()
    ect = ECT()
    gpe = GPE()

    r1 = three_dfit.estimate(
        events
    )

    r2 = ect.estimate(
        events
    )

    r3 = gpe.estimate(
        events
    )

    print()

    print(
        "Ground Truth:",
        cfg.freq
    )

    print(
        "3DFIT:",
        r1["frequency"]
    )

    print(
        "ECT:",
        r2["frequency"]
    )

    print(
        "GPE:",
        r3["frequency"]
    )


if __name__ == "__main__":
    main()
