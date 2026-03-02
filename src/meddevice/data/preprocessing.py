"""Basic signal preprocessing utilities for medical device time-series data."""

import numpy as np
import pandas as pd


def normalize(signal: np.ndarray) -> np.ndarray:
    """Min-max normalize a 1-D signal to the [0, 1] range.

    Parameters
    ----------
    signal:
        1-D NumPy array of raw sensor values.

    Returns
    -------
    np.ndarray
        Normalized signal.  If all values are equal the array is returned
        as-is (all zeros after subtraction) to avoid division by zero.
    """
    s_min = signal.min()
    s_max = signal.max()
    if s_max == s_min:
        return np.zeros_like(signal, dtype=float)
    return (signal - s_min) / (s_max - s_min)


def remove_baseline_wander(signal: np.ndarray, window: int = 200) -> np.ndarray:
    """Remove low-frequency baseline wander using a rolling-mean subtraction.

    Parameters
    ----------
    signal:
        1-D NumPy array (e.g. ECG samples).
    window:
        Size of the rolling window (samples) used to estimate the baseline.

    Returns
    -------
    np.ndarray
        Signal with baseline removed.
    """
    series = pd.Series(signal.astype(float))
    baseline = series.rolling(window=window, center=True, min_periods=1).mean()
    return (series - baseline).to_numpy()
