#!/usr/bin/env python3
"""
Lab 5: DataFrame Basics
GGY3061 - Introduction to Programming for Geologists

This module covers the fundamentals of pandas DataFrames:
- Creating DataFrames from dictionaries
- Reading CSV files
- Understanding DataFrame structure
- Basic inspection methods

Learning Outcome: LO5.1 - Create and manipulate DataFrames
"""

import pandas as pd
from pathlib import Path
from typing import Dict, List, Any, Optional


def create_sample_dataframe(data: Dict[str, List[Any]]) -> pd.DataFrame:
    """
    Create a pandas DataFrame from a dictionary.

    The dictionary should have column names as keys and lists of values
    as values. All lists must have the same length.

    Args:
        data: Dictionary with column names as keys and lists of values
              Example: {'name': ['A', 'B'], 'value': [1, 2]}

    Returns:
        pd.DataFrame: A new DataFrame created from the dictionary

    Example:
        >>> data = {
        ...     'sample_id': ['GEO-001', 'GEO-002', 'GEO-003'],
        ...     'rock_type': ['Granite', 'Basalt', 'Sandstone'],
        ...     'grade': [2.5, 1.8, 3.2]
        ... }
        >>> df = create_sample_dataframe(data)
        >>> len(df)
        3
    """
    # TODO: Create and return a DataFrame from the dictionary
    # Hint: Use pd.DataFrame() constructor
    pass


def read_drilling_data(filepath: str) -> pd.DataFrame:
    """
    Read drilling data from a CSV file into a DataFrame.

    Args:
        filepath: Path to the CSV file

    Returns:
        pd.DataFrame: DataFrame containing the CSV data

    Raises:
        FileNotFoundError: If the file does not exist

    Example:
        >>> df = read_drilling_data('data/drilling_data.csv')
        >>> 'sample_id' in df.columns
        True
    """
    # TODO: Read the CSV file and return the DataFrame
    # Hint: Use pd.read_csv()
    pass


def get_dataframe_info(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Extract basic information about a DataFrame.

    Returns a dictionary containing:
    - 'num_rows': Number of rows
    - 'num_cols': Number of columns
    - 'columns': List of column names
    - 'dtypes': Dictionary of column names to their data types (as strings)
    - 'memory_usage': Total memory usage in bytes

    Args:
        df: Input DataFrame

    Returns:
        Dict with DataFrame information

    Example:
        >>> data = {'a': [1, 2], 'b': ['x', 'y']}
        >>> df = pd.DataFrame(data)
        >>> info = get_dataframe_info(df)
        >>> info['num_rows']
        2
        >>> info['num_cols']
        2
    """
    # TODO: Extract and return DataFrame information
    # Hints:
    # - Use df.shape for dimensions
    # - Use df.columns for column names
    # - Use df.dtypes for data types
    # - Use df.memory_usage(deep=True).sum() for memory
    pass


def display_first_n_rows(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Return the first n rows of a DataFrame.

    Args:
        df: Input DataFrame
        n: Number of rows to return (default 5)

    Returns:
        pd.DataFrame: First n rows of the input DataFrame

    Example:
        >>> df = pd.DataFrame({'a': range(10)})
        >>> result = display_first_n_rows(df, 3)
        >>> len(result)
        3
    """
    # TODO: Return the first n rows
    # Hint: Use df.head()
    pass


def display_last_n_rows(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Return the last n rows of a DataFrame.

    Args:
        df: Input DataFrame
        n: Number of rows to return (default 5)

    Returns:
        pd.DataFrame: Last n rows of the input DataFrame

    Example:
        >>> df = pd.DataFrame({'a': range(10)})
        >>> result = display_last_n_rows(df, 3)
        >>> list(result['a'])
        [7, 8, 9]
    """
    # TODO: Return the last n rows
    # Hint: Use df.tail()
    pass


def get_column_names(df: pd.DataFrame) -> List[str]:
    """
    Get a list of all column names in the DataFrame.

    Args:
        df: Input DataFrame

    Returns:
        List of column names as strings

    Example:
        >>> df = pd.DataFrame({'a': [1], 'b': [2], 'c': [3]})
        >>> get_column_names(df)
        ['a', 'b', 'c']
    """
    # TODO: Return column names as a list
    # Hint: Use df.columns and convert to list
    pass


def get_numeric_columns(df: pd.DataFrame) -> List[str]:
    """
    Get a list of column names that contain numeric data.

    Args:
        df: Input DataFrame

    Returns:
        List of numeric column names

    Example:
        >>> df = pd.DataFrame({
        ...     'name': ['A', 'B'],
        ...     'value': [1.5, 2.5],
        ...     'count': [10, 20]
        ... })
        >>> get_numeric_columns(df)
        ['value', 'count']
    """
    # TODO: Return names of numeric columns
    # Hint: Use df.select_dtypes(include='number')
    pass


def check_missing_values(df: pd.DataFrame) -> Dict[str, int]:
    """
    Check for missing values in each column.

    Args:
        df: Input DataFrame

    Returns:
        Dictionary mapping column names to count of missing values

    Example:
        >>> df = pd.DataFrame({
        ...     'a': [1, None, 3],
        ...     'b': ['x', 'y', 'z']
        ... })
        >>> missing = check_missing_values(df)
        >>> missing['a']
        1
        >>> missing['b']
        0
    """
    # TODO: Count missing values per column
    # Hint: Use df.isnull().sum()
    pass


def set_index_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Set a column as the DataFrame index.

    Args:
        df: Input DataFrame
        column: Name of column to use as index

    Returns:
        DataFrame with the specified column as index

    Example:
        >>> df = pd.DataFrame({
        ...     'id': ['A', 'B', 'C'],
        ...     'value': [1, 2, 3]
        ... })
        >>> result = set_index_column(df, 'id')
        >>> result.index.name
        'id'
    """
    # TODO: Set the specified column as the index
    # Hint: Use df.set_index()
    pass


def reset_dataframe_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reset the DataFrame index to default integer index.

    Args:
        df: Input DataFrame with custom index

    Returns:
        DataFrame with default integer index, old index as column

    Example:
        >>> df = pd.DataFrame({'value': [1, 2]}, index=['A', 'B'])
        >>> result = reset_dataframe_index(df)
        >>> list(result.columns)
        ['index', 'value']
    """
    # TODO: Reset the index
    # Hint: Use df.reset_index()
    pass


# =============================================================================
# Main execution for testing
# =============================================================================

if __name__ == "__main__":
    # Test your implementations here
    print("Testing DataFrame Basics...")

    # Test create_sample_dataframe
    sample_data = {
        'sample_id': ['GEO-001', 'GEO-002', 'GEO-003'],
        'rock_type': ['Granite', 'Basalt', 'Sandstone'],
        'grade': [2.5, 1.8, 3.2],
        'depth': [150, 280, 95]
    }

    df = create_sample_dataframe(sample_data)
    if df is not None:
        print(f"Created DataFrame with shape: {df.shape}")
        print(df)
    else:
        print("create_sample_dataframe not implemented yet")

    # Test read_drilling_data
    try:
        drilling_df = read_drilling_data('data/drilling_data.csv')
        if drilling_df is not None:
            print(f"\nLoaded drilling data: {drilling_df.shape[0]} rows")
            print(drilling_df.head())
    except (FileNotFoundError, TypeError) as e:
        print(f"\nCould not load drilling data: {e}")

    print("\nDataFrame Basics module tests complete.")
