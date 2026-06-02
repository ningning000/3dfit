# metrics/frequency.py

def frequency_error(
    gt_frequency,
    estimated_frequency
):
    """
    Absolute frequency error (Hz)
    """

    return abs(
        estimated_frequency
        -
        gt_frequency
    )


def frequency_relative_error(
    gt_frequency,
    estimated_frequency
):
    """
    Relative frequency error (%)
    """

    return (
        abs(
            estimated_frequency
            -
            gt_frequency
        )
        /
        gt_frequency
        * 100.0
    )
