#!/usr/bin/env python3
"""
Lab 5: Descriptive Statistics
GGY3061 - Introduction to Programming for Geologists

This module covers statistical analysis with pandas:
- Using describe() for quick statistics
- Individual statistical methods
- Correlation analysis
- Handling missing data in statistics

Learning Outcome: LO5.4 - Generate descriptive statistics
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional


def get_summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get summary statistics for all numeric columns using describe().

    Args:
        df: Input DataFrame

    Returns:
        pd.DataFrame: Summary statistics (count, mean, std, min, 25%, 50%, 75%, max)

    Example:
        >>> df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [10, 20, 30, 40, 50]})
        >>> stats = get_summary_statistics(df)
        >>> 'mean' in stats.index
        True
    """
    # TODO: Return summary statistics
    # Hint: Use df.describe()
    pass


def calculate_column_mean(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the mean of a specific column.

    Args:
        df: Input DataFrame
        column: Column name

    Returns:
        float: Mean value

    Example:
        >>> df = pd.DataFrame({'grade': [1.0, 2.0, 3.0, 4.0, 5.0]})
        >>> calculate_column_mean(df, 'grade')
        3.0
    """
    # TODO: Calculate mean
    # Hint: Use df[column].mean()
    pass


def calculate_column_std(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the standard deviation of a specific column.

    Args:
        df: Input DataFrame
        column: Column name

    Returns:
        float: Standard deviation

    Example:
        >>> df = pd.DataFrame({'grade': [1.0, 2.0, 3.0, 4.0, 5.0]})
        >>> std = calculate_column_std(df, 'grade')
        >>> round(std, 2)
        1.58
    """
    # TODO: Calculate standard deviation
    # Hint: Use df[column].std()
    pass


def calculate_column_median(df: pd.DataFrame, column: str) -> float:
    """
    Calculate the median of a specific column.

    Args:
        df: Input DataFrame
        column: Column name

    Returns:
        float: Median value

    Example:
        >>> df = pd.DataFrame({'grade': [1.0, 2.0, 3.0, 4.0, 5.0]})
        >>> calculate_column_median(df, 'grade')
        3.0
    """
    # TODO: Calculate median
    # Hint: Use df[column].median()
    pass


def calculate_min_max(df: pd.DataFrame, column: str) -> Dict[str, float]:
    """
    Calculate minimum and maximum values of a column.

    Args:
        df: Input DataFrame
        column: Column name

    Returns:
        Dict with 'min' and 'max' keys

    Example:
        >>> df = pd.DataFrame({'grade': [1.0, 2.0, 3.0, 4.0, 5.0]})
        >>> result = calculate_min_max(df, 'grade')
        >>> result['min']
        1.0
        >>> result['max']
        5.0
    """
    # TODO: Calculate min and max
    # Hint: Use df[column].min() and df[column].max()
    pass


def calculate_percentiles(df: pd.DataFrame,
                          column: str,
                          percentiles: List[float]) -> Dict[float, float]:
    """
    Calculate specific percentiles of a column.

    Args:
        df: Input DataFrame
        column: Column name
        percentiles: List of percentiles (0-100)

    Returns:
        Dict mapping percentile to value

    Example:
        >>> df = pd.DataFrame({'grade': range(1, 101)})
        >>> result = calculate_percentiles(df, 'grade', [25, 50, 75])
        >>> result[50]
        50.5
    """
    # TODO: Calculate percentiles
    # Hint: Use df[column].quantile(p/100) for each percentile
    pass


def calculate_correlations(df: pd.DataFrame,
                            columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Calculate correlation matrix for numeric columns.

    Args:
        df: Input DataFrame
        columns: Optional list of columns (if None, use all numeric)

    Returns:
        pd.DataFrame: Correlation matrix

    Example:
        >>> df = pd.DataFrame({
        ...     'a': [1, 2, 3, 4, 5],
        ...     'b': [2, 4, 6, 8, 10]
        ... })
        >>> corr = calculate_correlations(df)
        >>> corr.loc['a', 'b']
        1.0
    """
    # TODO: Calculate correlations
    # Hint: Use df[columns].corr() or df.corr()
    pass


def find_highly_correlated(df: pd.DataFrame,
                            threshold: float = 0.7) -> List[tuple]:
    """
    Find pairs of columns with correlation above threshold.

    Args:
        df: Input DataFrame
        threshold: Correlation threshold (default 0.7)

    Returns:
        List of tuples (col1, col2, correlation) for pairs above threshold
        Only includes each pair once (not both (a,b) and (b,a))
        Excludes self-correlations

    Example:
        >>> df = pd.DataFrame({
        ...     'a': [1, 2, 3, 4, 5],
        ...     'b': [2, 4, 6, 8, 10],
        ...     'c': [5, 4, 3, 2, 1]
        ... })
        >>> result = find_highly_correlated(df, threshold=0.9)
        >>> ('a', 'b', 1.0) in result or ('b', 'a', 1.0) in result
        True
    """
    # TODO: Find highly correlated pairs
    # Hint: Get correlation matrix, iterate through upper triangle
    pass


def find_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Find outliers using the IQR method.

    Outliers are values below Q1 - 1.5*IQR or above Q3 + 1.5*IQR.

    Args:
        df: Input DataFrame
        column: Column to check for outliers

    Returns:
        pd.DataFrame: Rows containing outliers

    Example:
        >>> df = pd.DataFrame({'grade': [1, 2, 3, 4, 5, 100]})  # 100 is outlier
        >>> outliers = find_outliers_iqr(df, 'grade')
        >>> 100 in outliers['grade'].values
        True
    """
    # TODO: Find outliers using IQR
    # Hint:
    # Q1 = df[column].quantile(0.25)
    # Q3 = df[column].quantile(0.75)
    # IQR = Q3 - Q1
    # Filter: (value < Q1 - 1.5*IQR) | (value > Q3 + 1.5*IQR)
    pass


def find_outliers_zscore(df: pd.DataFrame,
                          column: str,
                          threshold: float = 3.0) -> pd.DataFrame:
    """
    Find outliers using z-score method.

    Outliers have absolute z-score above threshold.
    z-score = (value - mean) / std

    Args:
        df: Input DataFrame
        column: Column to check for outliers
        threshold: Z-score threshold (default 3.0)

    Returns:
        pd.DataFrame: Rows containing outliers

    Example:
        >>> df = pd.DataFrame({'grade': [1, 2, 3, 4, 5, 100]})
        >>> outliers = find_outliers_zscore(df, 'grade', threshold=2.0)
        >>> 100 in outliers['grade'].values
        True
    """
    # TODO: Find outliers using z-score
    # Hint: Calculate z-scores, filter by absolute value > threshold
    pass


def calculate_skewness(df: pd.DataFrame, column: str) -> float:
    """
    Calculate skewness of a column.

    Skewness indicates asymmetry of the distribution:
    - Positive: Right-skewed (tail on right)
    - Negative: Left-skewed (tail on left)
    - Near 0: Symmetric

    Args:
        df: Input DataFrame
        column: Column name

    Returns:
        float: Skewness value

    Example:
        >>> df = pd.DataFrame({'grade': [1, 1, 1, 2, 2, 3, 10]})
        >>> skew = calculate_skewness(df, 'grade')
        >>> skew > 0  # Right-skewed due to outlier
        True
    """
    # TODO: Calculate skewness
    # Hint: Use df[column].skew()
    pass


def calculate_kurtosis(df: pd.DataFrame, column: str) -> float:
    """
    Calculate kurtosis of a column.

    Kurtosis measures "tailedness" of distribution:
    - Positive: Heavy tails (more outliers)
    - Negative: Light tails (fewer outliers)
    - 0: Similar to normal distribution

    Args:
        df: Input DataFrame
        column: Column name

    Returns:
        float: Kurtosis value (excess kurtosis)

    Example:
        >>> df = pd.DataFrame({'grade': [1, 2, 3, 4, 5]})
        >>> kurt = calculate_kurtosis(df, 'grade')
        >>> isinstance(kurt, float)
        True
    """
    # TODO: Calculate kurtosis
    # Hint: Use df[column].kurtosis()
    pass


def count_missing_by_column(df: pd.DataFrame) -> pd.Series:
    """
    Count missing values in each column.

    Args:
        df: Input DataFrame

    Returns:
        pd.Series: Count of missing values per column

    Example:
        >>> df = pd.DataFrame({
        ...     'a': [1, None, 3],
        ...     'b': [None, None, 3]
        ... })
        >>> result = count_missing_by_column(df)
        >>> result['b']
        2
    """
    # TODO: Count missing values
    # Hint: Use df.isnull().sum()
    pass


def calculate_stats_excluding_missing(df: pd.DataFrame,
                                       column: str) -> Dict[str, float]:
    """
    Calculate statistics excluding missing values.

    Returns mean, std, min, max, count of non-missing values.

    Args:
        df: Input DataFrame
        column: Column name

    Returns:
        Dict with 'mean', 'std', 'min', 'max', 'count' keys

    Example:
        >>> df = pd.DataFrame({'grade': [1.0, None, 3.0, None, 5.0]})
        >>> stats = calculate_stats_excluding_missing(df, 'grade')
        >>> stats['count']
        3.0
    """
    # TODO: Calculate statistics excluding NaN
    # Hint: pandas methods automatically exclude NaN by default
    pass


def calculate_grouped_statistics(df: pd.DataFrame,
                                  group_col: str,
                                  value_col: str) -> pd.DataFrame:
    """
    Calculate comprehensive statistics for each group.

    Returns: count, mean, std, min, 25%, 50%, 75%, max for each group.

    Args:
        df: Input DataFrame
        group_col: Column to group by
        value_col: Column to calculate statistics for

    Returns:
        pd.DataFrame: Statistics for each group

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt', 'Basalt'],
        ...     'grade': [2.0, 3.0, 1.5, 2.5]
        ... })
        >>> stats = calculate_grouped_statistics(df, 'rock_type', 'grade')
        >>> 'mean' in stats.columns
        True
    """
    # TODO: Calculate grouped statistics
    # Hint: Use df.groupby(group_col)[value_col].describe()
    pass


# =============================================================================
# Main execution for testing
# =============================================================================

if __name__ == "__main__":
    # Test your implementations here
    print("Testing Descriptive Statistics...")

    # Create test data with some characteristics
    np.random.seed(42)
    test_df = pd.DataFrame({
        'sample_id': [f'GEO-{i:03d}' for i in range(1, 51)],
        'rock_type': np.random.choice(['Granite', 'Basalt', 'Schist'], 50),
        'grade': np.random.exponential(2, 50),  # Right-skewed
        'depth': np.random.normal(300, 100, 50),
        'mass': np.random.uniform(10, 25, 50)
    })

    # Add some missing values
    test_df.loc[5, 'grade'] = np.nan
    test_df.loc[15, 'depth'] = np.nan

    # Add an outlier
    test_df.loc[0, 'grade'] = 50.0

    print("Test DataFrame shape:", test_df.shape)
    print("\nFirst few rows:")
    print(test_df.head())

    # Test get_summary_statistics
    stats = get_summary_statistics(test_df)
    if stats is not None:
        print("\nSummary Statistics:")
        print(stats)
    else:
        print("\nget_summary_statistics not implemented yet")

    # Test find_outliers_iqr
    outliers = find_outliers_iqr(test_df, 'grade')
    if outliers is not None:
        print(f"\nOutliers found (IQR method): {len(outliers)} rows")
        print(outliers[['sample_id', 'grade']])
    else:
        print("\nfind_outliers_iqr not implemented yet")

    # Test calculate_correlations
    corr = calculate_correlations(test_df)
    if corr is not None:
        print("\nCorrelation Matrix:")
        print(corr)
    else:
        print("\ncalculate_correlations not implemented yet")

    print("\nDescriptive Statistics module tests complete.")
