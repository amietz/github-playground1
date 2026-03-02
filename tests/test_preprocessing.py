"""Tests for meddevice.data.preprocessing."""

import numpy as np
import pytest

from meddevice.data.preprocessing import normalize, remove_baseline_wander


class TestNormalize:
    def test_basic_range(self):
        signal = np.array([0.0, 5.0, 10.0])
        result = normalize(signal)
        assert result[0] == pytest.approx(0.0)
        assert result[-1] == pytest.approx(1.0)

    def test_constant_signal(self):
        signal = np.array([3.0, 3.0, 3.0])
        result = normalize(signal)
        assert np.all(result == 0.0)

    def test_output_shape(self):
        signal = np.random.rand(100)
        assert normalize(signal).shape == signal.shape


class TestRemoveBaselineWander:
    def test_output_shape(self):
        signal = np.sin(np.linspace(0, 4 * np.pi, 500))
        result = remove_baseline_wander(signal, window=50)
        assert result.shape == signal.shape

    def test_zero_mean_approx(self):
        """After baseline removal the mean of a pure sine should be near zero."""
        t = np.linspace(0, 4 * np.pi, 500)
        signal = np.sin(t)
        result = remove_baseline_wander(signal, window=50)
        assert abs(result.mean()) < 0.1
