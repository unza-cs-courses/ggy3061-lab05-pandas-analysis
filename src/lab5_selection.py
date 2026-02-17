#!/usr/bin/env python3
"""
Lab 5: Data Selection and Filtering
GGY3061 - Introduction to Programming for Geologists

This module covers data selection techniques in pandas:
- Column selection with bracket notation
- Row selection with loc and iloc
- Boolean indexing for filtering
- Combining multiple conditions

Learning Outcome: LO5.2 - Select and filter data effectively
"""

import pandas as pd
from typing import List, Any, Union


def select_single_column(df: pd.DataFrame, column: str) -> pd.Series:
    """
    Select a single column from a DataFrame.

    Args:
        df: Input DataFrame
        column: Name of the column to select

    Returns:
        pd.Series: The selected column as a Series

    Example:
        >>> df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        >>> series = select_single_column(df, 'a')
        >>> list(series)
        [1, 2]
    """
    # TODO: Select and return a single column
    # Hint: Use df[column] or df.loc[:, column]
    pass


def select_multiple_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Select multiple columns from a DataFrame.

    Args:
        df: Input DataFrame
        columns: List of column names to select

    Returns:
        pd.DataFrame: DataFrame with only the selected columns

    Example:
        >>> df = pd.DataFrame({'a': [1], 'b': [2], 'c': [3]})
        >>> result = select_multiple_columns(df, ['a', 'c'])
        >>> list(result.columns)
        ['a', 'c']
    """
    # TODO: Select and return multiple columns
    # Hint: Use df[columns] with a list of column names
    pass


def select_rows_by_position(df: pd.DataFrame, start: int, end: int) -> pd.DataFrame:
    """
    Select rows by their integer position (slice).

    Args:
        df: Input DataFrame
        start: Starting index (inclusive)
        end: Ending index (exclusive)

    Returns:
        pd.DataFrame: Rows from start to end-1

    Example:
        >>> df = pd.DataFrame({'a': range(10)})
        >>> result = select_rows_by_position(df, 2, 5)
        >>> list(result['a'])
        [2, 3, 4]
    """
    # TODO: Select rows by position
    # Hint: Use df.iloc[start:end]
    pass


def select_rows_by_label(df: pd.DataFrame, labels: List[Any]) -> pd.DataFrame:
    """
    Select rows by their index labels.

    Args:
        df: Input DataFrame (may have non-integer index)
        labels: List of index labels to select

    Returns:
        pd.DataFrame: Rows matching the specified labels

    Example:
        >>> df = pd.DataFrame({'value': [10, 20, 30]}, index=['a', 'b', 'c'])
        >>> result = select_rows_by_label(df, ['a', 'c'])
        >>> list(result['value'])
        [10, 30]
    """
    # TODO: Select rows by label
    # Hint: Use df.loc[labels]
    pass


def filter_by_value(df: pd.DataFrame, column: str, value: Any) -> pd.DataFrame:
    """
    Filter DataFrame to rows where column equals value.

    Args:
        df: Input DataFrame
        column: Column to filter on
        value: Value to match

    Returns:
        pd.DataFrame: Filtered DataFrame

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Basalt', 'Granite'],
        ...     'grade': [2.0, 1.5, 3.0]
        ... })
        >>> result = filter_by_value(df, 'rock_type', 'Granite')
        >>> len(result)
        2
    """
    # TODO: Filter rows where column equals value
    # Hint: Use boolean indexing df[df[column] == value]
    pass


def filter_greater_than(df: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
    """
    Filter DataFrame to rows where column is greater than threshold.

    Args:
        df: Input DataFrame
        column: Numeric column to filter on
        threshold: Minimum value (exclusive)

    Returns:
        pd.DataFrame: Filtered DataFrame

    Example:
        >>> df = pd.DataFrame({'grade': [1.0, 2.0, 3.0, 4.0]})
        >>> result = filter_greater_than(df, 'grade', 2.5)
        >>> list(result['grade'])
        [3.0, 4.0]
    """
    # TODO: Filter rows where column > threshold
    # Hint: Use df[df[column] > threshold]
    pass


def filter_between(df: pd.DataFrame, column: str,
                   lower: float, upper: float) -> pd.DataFrame:
    """
    Filter DataFrame to rows where column is between lower and upper (inclusive).

    Args:
        df: Input DataFrame
        column: Numeric column to filter on
        lower: Lower bound (inclusive)
        upper: Upper bound (inclusive)

    Returns:
        pd.DataFrame: Filtered DataFrame

    Example:
        >>> df = pd.DataFrame({'depth': [100, 200, 300, 400, 500]})
        >>> result = filter_between(df, 'depth', 200, 400)
        >>> len(result)
        3
    """
    # TODO: Filter rows where lower <= column <= upper
    # Hint: Use df[(df[column] >= lower) & (df[column] <= upper)]
    # Or use df[column].between(lower, upper)
    pass


def filter_in_list(df: pd.DataFrame, column: str, values: List[Any]) -> pd.DataFrame:
    """
    Filter DataFrame to rows where column value is in the given list.

    Args:
        df: Input DataFrame
        column: Column to filter on
        values: List of values to include

    Returns:
        pd.DataFrame: Filtered DataFrame

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Basalt', 'Schist', 'Gneiss']
        ... })
        >>> result = filter_in_list(df, 'rock_type', ['Granite', 'Basalt'])
        >>> len(result)
        2
    """
    # TODO: Filter rows where column value is in the list
    # Hint: Use df[df[column].isin(values)]
    pass


def filter_multiple_conditions(df: pd.DataFrame,
                                rock_type: str,
                                min_grade: float) -> pd.DataFrame:
    """
    Filter DataFrame with multiple conditions (AND logic).

    Select rows where:
    - rock_type column equals the specified rock_type
    - grade column is greater than or equal to min_grade

    Args:
        df: Input DataFrame with 'rock_type' and 'grade' columns
        rock_type: Rock type to filter for
        min_grade: Minimum grade threshold (inclusive)

    Returns:
        pd.DataFrame: Filtered DataFrame

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt'],
        ...     'grade': [1.0, 3.0, 2.0]
        ... })
        >>> result = filter_multiple_conditions(df, 'Granite', 2.0)
        >>> len(result)
        1
    """
    # TODO: Filter with multiple conditions
    # Hint: Use & to combine conditions
    # df[(condition1) & (condition2)]
    pass


def filter_or_conditions(df: pd.DataFrame,
                         column: str,
                         value1: Any,
                         value2: Any) -> pd.DataFrame:
    """
    Filter DataFrame with OR logic.

    Select rows where column equals value1 OR value2.

    Args:
        df: Input DataFrame
        column: Column to filter on
        value1: First value to match
        value2: Second value to match

    Returns:
        pd.DataFrame: Filtered DataFrame

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Basalt', 'Schist', 'Gneiss']
        ... })
        >>> result = filter_or_conditions(df, 'rock_type', 'Granite', 'Basalt')
        >>> len(result)
        2
    """
    # TODO: Filter with OR logic
    # Hint: Use | to combine conditions
    # df[(condition1) | (condition2)]
    pass


def filter_not_null(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Filter DataFrame to rows where column is not null/NaN.

    Args:
        df: Input DataFrame
        column: Column to check for null values

    Returns:
        pd.DataFrame: Filtered DataFrame without null values in column

    Example:
        >>> df = pd.DataFrame({'grade': [1.0, None, 3.0, None]})
        >>> result = filter_not_null(df, 'grade')
        >>> len(result)
        2
    """
    # TODO: Filter out null values
    # Hint: Use df[df[column].notna()] or df[~df[column].isna()]
    pass


def select_rows_and_columns(df: pd.DataFrame,
                            row_condition: pd.Series,
                            columns: List[str]) -> pd.DataFrame:
    """
    Select specific columns for rows matching a condition.

    Args:
        df: Input DataFrame
        row_condition: Boolean Series for row selection
        columns: List of columns to select

    Returns:
        pd.DataFrame: Selected rows and columns

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Basalt'],
        ...     'grade': [2.0, 1.5],
        ...     'depth': [100, 200]
        ... })
        >>> condition = df['grade'] > 1.5
        >>> result = select_rows_and_columns(df, condition, ['rock_type', 'grade'])
        >>> list(result.columns)
        ['rock_type', 'grade']
    """
    # TODO: Select rows by condition and specific columns
    # Hint: Use df.loc[row_condition, columns]
    pass


def get_unique_values(df: pd.DataFrame, column: str) -> List[Any]:
    """
    Get all unique values from a column.

    Args:
        df: Input DataFrame
        column: Column to get unique values from

    Returns:
        List of unique values

    Example:
        >>> df = pd.DataFrame({'rock_type': ['Granite', 'Basalt', 'Granite']})
        >>> sorted(get_unique_values(df, 'rock_type'))
        ['Basalt', 'Granite']
    """
    # TODO: Get unique values from column
    # Hint: Use df[column].unique() and convert to list
    pass


def count_unique_values(df: pd.DataFrame, column: str) -> pd.Series:
    """
    Count occurrences of each unique value in a column.

    Args:
        df: Input DataFrame
        column: Column to count values in

    Returns:
        pd.Series: Counts of each unique value

    Example:
        >>> df = pd.DataFrame({'rock_type': ['Granite', 'Basalt', 'Granite']})
        >>> counts = count_unique_values(df, 'rock_type')
        >>> counts['Granite']
        2
    """
    # TODO: Count value occurrences
    # Hint: Use df[column].value_counts()
    pass


# =============================================================================
# Main execution for testing
# =============================================================================

if __name__ == "__main__":
    # Test your implementations here
    print("Testing Data Selection...")

    # Create test data
    test_df = pd.DataFrame({
        'sample_id': ['GEO-001', 'GEO-002', 'GEO-003', 'GEO-004', 'GEO-005'],
        'rock_type': ['Granite', 'Basalt', 'Granite', 'Schist', 'Basalt'],
        'grade': [2.5, 1.8, 3.2, 0.9, 2.1],
        'depth': [150, 280, 95, 420, 310]
    })

    print("Test DataFrame:")
    print(test_df)

    # Test filter_greater_than
    result = filter_greater_than(test_df, 'grade', 2.0)
    if result is not None:
        print(f"\nFiltered (grade > 2.0): {len(result)} rows")
        print(result)
    else:
        print("\nfilter_greater_than not implemented yet")

    # Test filter_multiple_conditions
    result = filter_multiple_conditions(test_df, 'Granite', 2.0)
    if result is not None:
        print(f"\nFiltered (Granite AND grade >= 2.0): {len(result)} rows")
        print(result)
    else:
        print("\nfilter_multiple_conditions not implemented yet")

    print("\nData Selection module tests complete.")
