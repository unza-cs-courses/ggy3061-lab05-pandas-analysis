#!/usr/bin/env python3
"""
Pytest configuration for Lab 5: Hidden Tests
GGY3061 - Introduction to Programming for Geologists

Provides fixtures for hidden tests that verify correctness against
the actual drilling data and student-specific variant parameters.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys
import json

# Add src directory to path for imports
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))


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
        pytest.skip("drilling_data.csv not found")


@pytest.fixture
def variant_config():
    """Load the student's variant configuration."""
    # Try loading from pre-generated config first (created by CI workflow)
    config_path = Path(__file__).parent.parent.parent / ".variant_config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)

    # Fall back to generating from get_variant.py
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "get_variant",
        str(Path(__file__).parent.parent.parent / "scripts" / "get_variant.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.get_my_variant()


@pytest.fixture
def alternative_dataframe():
    """Provide alternative test data to catch hardcoded return values."""
    np.random.seed(99)
    return pd.DataFrame({
        'sample_id': [f'ALT-{i:03d}' for i in range(1, 21)],
        'rock_type': np.random.choice(['Marble', 'Slate', 'Quartzite'], 20),
        'grade': np.round(np.random.uniform(0.5, 5.0, 20), 2),
        'depth': np.random.randint(50, 600, 20),
        'mass': np.round(np.random.uniform(8, 25, 20), 1),
        'location': np.random.choice(['Mine-X', 'Mine-Y'], 20)
    })


@pytest.fixture
def dataframe_with_nulls():
    """Provide a DataFrame with missing values for hidden testing."""
    return pd.DataFrame({
        'sample_id': [f'NULL-{i:03d}' for i in range(1, 9)],
        'rock_type': ['Granite', 'Basalt', None, 'Schist', 'Basalt', None, 'Granite', 'Schist'],
        'grade': [2.5, None, 3.2, 0.9, None, 1.8, None, 4.1],
        'depth': [150, 280, None, 420, 310, 200, 175, None],
        'mass': [12.5, 15.3, 10.8, None, 14.1, 11.2, None, 16.7]
    })


# Cleanup matplotlib figures after tests
@pytest.fixture(autouse=True)
def cleanup_plots():
    """Clean up matplotlib figures after each test."""
    import matplotlib.pyplot as plt
    yield
    plt.close('all')
