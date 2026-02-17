#!/usr/bin/env python3
"""
Lab 5: GroupBy Operations
GGY3061 - Introduction to Programming for Geologists

This module covers pandas groupby operations:
- Basic groupby and aggregation
- Multiple aggregation functions
- Named aggregations
- Transformations within groups

Learning Outcome: LO5.3 - Perform groupby operations and aggregations
"""

import pandas as pd
from typing import List, Dict, Any, Callable


def group_and_mean(df: pd.DataFrame, group_col: str, value_col: str) -> pd.Series:
    """
    Group by a column and calculate the mean of another column.

    Args:
        df: Input DataFrame
        group_col: Column to group by
        value_col: Column to calculate mean for

    Returns:
        pd.Series: Mean values indexed by group

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Basalt', 'Granite', 'Basalt'],
        ...     'grade': [2.0, 1.5, 3.0, 2.5]
        ... })
        >>> result = group_and_mean(df, 'rock_type', 'grade')
        >>> result['Granite']
        2.5
    """
    # TODO: Group by group_col and calculate mean of value_col
    # Hint: Use df.groupby(group_col)[value_col].mean()
    pass


def group_and_sum(df: pd.DataFrame, group_col: str, value_col: str) -> pd.Series:
    """
    Group by a column and calculate the sum of another column.

    Args:
        df: Input DataFrame
        group_col: Column to group by
        value_col: Column to calculate sum for

    Returns:
        pd.Series: Sum values indexed by group

    Example:
        >>> df = pd.DataFrame({
        ...     'location': ['Site-A', 'Site-B', 'Site-A'],
        ...     'mass': [10.0, 15.0, 20.0]
        ... })
        >>> result = group_and_sum(df, 'location', 'mass')
        >>> result['Site-A']
        30.0
    """
    # TODO: Group and sum
    # Hint: Use df.groupby(group_col)[value_col].sum()
    pass


def group_and_count(df: pd.DataFrame, group_col: str) -> pd.Series:
    """
    Count the number of records in each group.

    Args:
        df: Input DataFrame
        group_col: Column to group by

    Returns:
        pd.Series: Count of records per group

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Basalt', 'Granite', 'Basalt', 'Granite']
        ... })
        >>> result = group_and_count(df, 'rock_type')
        >>> result['Granite']
        3
    """
    # TODO: Count records per group
    # Hint: Use df.groupby(group_col).size()
    pass


def group_and_aggregate(df: pd.DataFrame,
                        group_col: str,
                        agg_dict: Dict[str, str]) -> pd.DataFrame:
    """
    Group by a column and apply different aggregations to different columns.

    Args:
        df: Input DataFrame
        group_col: Column to group by
        agg_dict: Dictionary mapping column names to aggregation functions
                  e.g., {'grade': 'mean', 'depth': 'max'}

    Returns:
        pd.DataFrame: Aggregated results

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt'],
        ...     'grade': [2.0, 3.0, 1.5],
        ...     'depth': [100, 200, 150]
        ... })
        >>> result = group_and_aggregate(df, 'rock_type', {'grade': 'mean', 'depth': 'max'})
        >>> result.loc['Granite', 'grade']
        2.5
    """
    # TODO: Apply different aggregations per column
    # Hint: Use df.groupby(group_col).agg(agg_dict)
    pass


def group_multiple_aggregations(df: pd.DataFrame,
                                 group_col: str,
                                 value_col: str) -> pd.DataFrame:
    """
    Group by a column and calculate multiple statistics for one column.

    Calculate: mean, std, min, max, count for the value column.

    Args:
        df: Input DataFrame
        group_col: Column to group by
        value_col: Column to aggregate

    Returns:
        pd.DataFrame: Statistics for each group

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt', 'Basalt'],
        ...     'grade': [2.0, 3.0, 1.5, 2.5]
        ... })
        >>> result = group_multiple_aggregations(df, 'rock_type', 'grade')
        >>> 'mean' in result.columns
        True
    """
    # TODO: Calculate multiple statistics per group
    # Hint: Use df.groupby(group_col)[value_col].agg(['mean', 'std', 'min', 'max', 'count'])
    pass


def group_and_first(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Get the first record from each group.

    Args:
        df: Input DataFrame
        group_col: Column to group by

    Returns:
        pd.DataFrame: First record from each group

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt'],
        ...     'sample_id': ['GEO-001', 'GEO-002', 'GEO-003']
        ... })
        >>> result = group_and_first(df, 'rock_type')
        >>> len(result)
        2
    """
    # TODO: Get first record per group
    # Hint: Use df.groupby(group_col).first()
    pass


def group_and_last(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Get the last record from each group.

    Args:
        df: Input DataFrame
        group_col: Column to group by

    Returns:
        pd.DataFrame: Last record from each group
    """
    # TODO: Get last record per group
    # Hint: Use df.groupby(group_col).last()
    pass


def top_n_per_group(df: pd.DataFrame,
                    group_col: str,
                    sort_col: str,
                    n: int = 3) -> pd.DataFrame:
    """
    Get top N records from each group based on a sort column.

    Args:
        df: Input DataFrame
        group_col: Column to group by
        sort_col: Column to sort by (descending)
        n: Number of records per group (default 3)

    Returns:
        pd.DataFrame: Top N records from each group

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Granite', 'Basalt', 'Basalt'],
        ...     'grade': [2.0, 3.0, 1.0, 1.5, 2.5]
        ... })
        >>> result = top_n_per_group(df, 'rock_type', 'grade', n=2)
        >>> len(result[result['rock_type'] == 'Granite'])
        2
    """
    # TODO: Get top N records per group
    # Hint: Use df.groupby(group_col).apply(lambda x: x.nlargest(n, sort_col))
    # Or use df.sort_values().groupby().head()
    pass


def group_and_transform(df: pd.DataFrame,
                         group_col: str,
                         value_col: str) -> pd.Series:
    """
    Calculate group mean and return it for each row (transform).

    Unlike aggregation, transform returns a Series with the same index
    as the input, where each value is replaced by the group statistic.

    Args:
        df: Input DataFrame
        group_col: Column to group by
        value_col: Column to calculate mean for

    Returns:
        pd.Series: Group means aligned with original index

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt'],
        ...     'grade': [2.0, 3.0, 1.5]
        ... })
        >>> result = group_and_transform(df, 'rock_type', 'grade')
        >>> result[0]  # First Granite row gets Granite mean
        2.5
    """
    # TODO: Transform to get group means for each row
    # Hint: Use df.groupby(group_col)[value_col].transform('mean')
    pass


def calculate_within_group_rank(df: pd.DataFrame,
                                 group_col: str,
                                 value_col: str) -> pd.Series:
    """
    Calculate rank within each group (1 = highest value in group).

    Args:
        df: Input DataFrame
        group_col: Column to group by
        value_col: Column to rank

    Returns:
        pd.Series: Ranks within each group

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Granite'],
        ...     'grade': [2.0, 3.0, 1.0]
        ... })
        >>> result = calculate_within_group_rank(df, 'rock_type', 'grade')
        >>> result[1]  # Grade 3.0 should be rank 1
        1.0
    """
    # TODO: Calculate rank within groups
    # Hint: Use df.groupby(group_col)[value_col].rank(ascending=False)
    pass


def group_by_multiple_columns(df: pd.DataFrame,
                               group_cols: List[str],
                               value_col: str) -> pd.Series:
    """
    Group by multiple columns and calculate mean.

    Args:
        df: Input DataFrame
        group_cols: List of columns to group by
        value_col: Column to calculate mean for

    Returns:
        pd.Series: Mean values indexed by multi-level index

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt'],
        ...     'location': ['Site-A', 'Site-B', 'Site-A'],
        ...     'grade': [2.0, 3.0, 1.5]
        ... })
        >>> result = group_by_multiple_columns(df, ['rock_type', 'location'], 'grade')
        >>> result[('Granite', 'Site-A')]
        2.0
    """
    # TODO: Group by multiple columns
    # Hint: Use df.groupby(group_cols)[value_col].mean()
    pass


def pivot_grouped_data(df: pd.DataFrame,
                        index_col: str,
                        columns_col: str,
                        values_col: str) -> pd.DataFrame:
    """
    Create a pivot table from grouped data.

    Args:
        df: Input DataFrame
        index_col: Column for row labels
        columns_col: Column for column labels
        values_col: Column for values (will calculate mean)

    Returns:
        pd.DataFrame: Pivot table

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt', 'Basalt'],
        ...     'location': ['Site-A', 'Site-B', 'Site-A', 'Site-B'],
        ...     'grade': [2.0, 3.0, 1.5, 2.5]
        ... })
        >>> result = pivot_grouped_data(df, 'rock_type', 'location', 'grade')
        >>> result.loc['Granite', 'Site-A']
        2.0
    """
    # TODO: Create a pivot table
    # Hint: Use pd.pivot_table(df, values=values_col, index=index_col,
    #                          columns=columns_col, aggfunc='mean')
    pass


# =============================================================================
# Main execution for testing
# =============================================================================

if __name__ == "__main__":
    # Test your implementations here
    print("Testing GroupBy Operations...")

    # Create test data
    test_df = pd.DataFrame({
        'sample_id': ['GEO-001', 'GEO-002', 'GEO-003', 'GEO-004', 'GEO-005', 'GEO-006'],
        'rock_type': ['Granite', 'Basalt', 'Granite', 'Schist', 'Basalt', 'Granite'],
        'location': ['Site-A', 'Site-A', 'Site-B', 'Site-A', 'Site-B', 'Site-A'],
        'grade': [2.5, 1.8, 3.2, 0.9, 2.1, 1.5],
        'depth': [150, 280, 95, 420, 310, 200]
    })

    print("Test DataFrame:")
    print(test_df)

    # Test group_and_mean
    result = group_and_mean(test_df, 'rock_type', 'grade')
    if result is not None:
        print("\nMean grade by rock type:")
        print(result)
    else:
        print("\ngroup_and_mean not implemented yet")

    # Test group_and_count
    result = group_and_count(test_df, 'rock_type')
    if result is not None:
        print("\nCount by rock type:")
        print(result)
    else:
        print("\ngroup_and_count not implemented yet")

    # Test group_multiple_aggregations
    result = group_multiple_aggregations(test_df, 'rock_type', 'grade')
    if result is not None:
        print("\nMultiple statistics by rock type:")
        print(result)
    else:
        print("\ngroup_multiple_aggregations not implemented yet")

    print("\nGroupBy Operations module tests complete.")
