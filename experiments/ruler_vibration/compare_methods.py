from .run_single import run_single


def compare_methods(config):

    results = run_single(config)

    print()

    print("========== Ruler Experiment ==========")

    for name, result in results.items():

        print(
            f"{name}: "
            f"Frequency = {result['frequency']:.3f} Hz"
        )

        if "amplitude" in result:

            print(
                f"        "
                f"Amplitude = {result['amplitude']:.3f}"
            )

    return results
