#!/usr/bin/env python3
"""
Pytest configuration for Lab 5: pandas Analysis
GGY3061 - Introduction to Programming for Geologists

This module provides shared fixtures and configuration for Lab 5 tests.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src directory to path for imports
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def sample_dataframe():
    """Provide a simple sample DataFrame for testing."""
    return pd.DataFrame({
        'sample_id': ['GEO-001', 'GEO-002', 'GEO-003', 'GEO-004', 'GEO-005'],
        'rock_type': ['Granite', 'Basalt', 'Granite', 'Schist', 'Basalt'],
        'grade': [2.5, 1.8, 3.2, 0.9, 2.1],
        'depth': [150, 280, 95, 420, 310],
        'mass': [12.5, 15.3, 10.8, 18.2, 14.1],
        'location': ['Site-A', 'Site-B', 'Site-A', 'Site-C', 'Site-B']
    })


@pytest.fixture
def larger_dataframe():
    """Provide a larger DataFrame for comprehensive testing."""
    np.random.seed(42)
    n = 50

    rock_types = ['Granite', 'Basalt', 'Schist', 'Gneiss', 'Sandstone']
    locations = ['Site-A', 'Site-B', 'Site-C']
    analysts = ['Smith', 'Johnson', 'Williams']

    return pd.DataFrame({
        'sample_id': [f'GEO-{i:03d}' for i in range(1, n + 1)],
        'hole_id': [f'DH-{np.random.randint(1, 6):02d}' for _ in range(n)],
        'rock_type': np.random.choice(rock_types, n),
        'grade': np.round(np.random.exponential(2, n), 2),
        'depth': np.random.randint(50, 500, n),
        'mass': np.round(np.random.uniform(8, 22, n), 1),
        'volume': np.round(np.random.uniform(3, 8, n), 1),
        'location': np.random.choice(locations, n),
        'analyst': np.random.choice(analysts, n)
    })


@pytest.fixture
def dataframe_with_nulls():
    """Provide a DataFrame with missing values for testing."""
    return pd.DataFrame({
        'sample_id': ['GEO-001', 'GEO-002', 'GEO-003', 'GEO-004', 'GEO-005'],
        'rock_type': ['Granite', 'Basalt', None, 'Schist', 'Basalt'],
        'grade': [2.5, None, 3.2, 0.9, None],
        'depth': [150, 280, None, 420, 310],
        'mass': [12.5, 15.3, 10.8, None, 14.1]
    })


@pytest.fixture
def dataframe_with_outliers():
    """Provide a DataFrame with outliers for testing."""
    return pd.DataFrame({
        'sample_id': [f'GEO-{i:03d}' for i in range(1, 11)],
        'grade': [2.0, 2.5, 2.2, 2.8, 2.1, 2.3, 2.6, 2.4, 50.0, 2.7],  # 50.0 is outlier
        'depth': [100, 150, 120, 180, 130, 160, 140, 170, 200, 190]
    })


@pytest.fixture
def drilling_data_path():
    """Provide path to the drilling data CSV file."""
    return Path(__file__).parent.parent.parent / "data" / "drilling_data.csv"


@pytest.fixture
def drilling_dataframe(drilling_data_path):
    """Load the actual drilling data for testing."""
    if drilling_data_path.exists():
        return pd.read_csv(drilling_data_path)
    else:
        # Return a mock DataFrame if file doesn't exist yet
        pytest.skip("drilling_data.csv not found")


@pytest.fixture
def numeric_only_dataframe():
    """Provide a DataFrame with only numeric columns for correlation tests."""
    np.random.seed(42)
    n = 30

    # Create correlated data
    x = np.random.randn(n)
    y = x * 2 + np.random.randn(n) * 0.5  # Strongly correlated with x
    z = np.random.randn(n)  # Uncorrelated

    return pd.DataFrame({
        'x': x,
        'y': y,
        'z': z
    })


@pytest.fixture
def grouped_dataframe():
    """Provide a DataFrame suitable for groupby testing."""
    return pd.DataFrame({
        'category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
        'value': [10, 20, 30, 15, 25, 35, 12, 22, 32],
        'weight': [1.0, 1.5, 2.0, 1.2, 1.8, 2.2, 1.1, 1.6, 2.1]
    })


# Test output directory
@pytest.fixture
def output_dir(tmp_path):
    """Provide a temporary directory for test outputs."""
    return tmp_path


# Cleanup matplotlib figures after tests
@pytest.fixture(autouse=True)
def cleanup_plots():
    """Clean up matplotlib figures after each test."""
    import matplotlib.pyplot as plt
    yield
    plt.close('all')
