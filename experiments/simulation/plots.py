# experiments/simulation/plots.py

import matplotlib.pyplot as plt


def plot_frequency_comparison(df):

    gt = df["gt_frequency"]

    plt.figure(
        figsize=(6, 5)
    )

    plt.plot(
        gt,
        gt,
        "k--",
        label="Ground Truth"
    )

    plt.scatter(
        gt,
        df["3dfit"],
        marker="^",
        s=80,
        label="3DFIT"
    )

    plt.scatter(
        gt,
        df["ect"],
        marker="o",
        s=80,
        label="ECT"
    )

    plt.scatter(
        gt,
        df["gpe"],
        marker="s",
        s=80,
        label="GPE"
    )

    plt.xlabel(
        "Ground Truth Frequency (Hz)"
    )

    plt.ylabel(
        "Estimated Frequency (Hz)"
    )

    plt.grid(alpha=0.3)

    plt.legend()

    plt.tight_layout()

    plt.show()
