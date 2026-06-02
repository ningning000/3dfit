import matplotlib.pyplot as plt


def plot_method_comparison(results):

    methods = list(
        results.keys()
    )

    freqs = [
        results[m]["frequency"]
        for m in methods
    ]

    plt.figure(
        figsize=(6,5)
    )

    plt.bar(
        methods,
        freqs
    )

    plt.ylabel(
        "Estimated Frequency (Hz)"
    )

    plt.tight_layout()

    plt.show()
