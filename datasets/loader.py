# datasets/loader.py

import h5py
import numpy as np


def load_events(file_path):
    """
    Load event camera data from HDF5.

    Parameters
    ----------
    file_path : str
        Path to hdf5 file.

    Returns
    -------
    events : dict
        {
            "x": ndarray,
            "y": ndarray,
            "t": ndarray (seconds),
            "p": ndarray or None
        }
    """

    with h5py.File(file_path, "r") as f:

        if "CD" not in f:
            raise ValueError("Group 'CD' not found.")

        if "events" not in f["CD"]:
            raise ValueError("Dataset 'CD/events' not found.")

        e = f["CD/events"][:]

        events = {
            "x": e["x"].astype(np.float64),
            "y": e["y"].astype(np.float64),
            "t": e["t"].astype(np.float64) * 1e-6
        }

        # polarity may exist
        if "p" in e.dtype.names:
            events["p"] = e["p"].astype(np.float64)
        else:
            events["p"] = None

    return events
