# metrics/amplitude.py

def amplitude_error(
    gt_amplitude,
    estimated_amplitude
):
    """
    Absolute amplitude error (pixel)
    """

    return abs(
        estimated_amplitude
        -
        gt_amplitude
    )


def amplitude_relative_error(
    gt_amplitude,
    estimated_amplitude
):
    """
    Relative amplitude error (%)
    """

    return (
        abs(
            estimated_amplitude
            -
            gt_amplitude
        )
        /
        gt_amplitude
        * 100.0
    )
