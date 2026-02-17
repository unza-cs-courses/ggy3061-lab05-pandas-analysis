#!/usr/bin/env python3
"""
Visible Tests for Lab 5: pandas Analysis
GGY3061 - Introduction to Programming for Geologists

These tests verify student implementations of pandas operations.
Students can see and run these tests locally.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path


# =============================================================================
# Part 1: DataFrame Basics Tests
# =============================================================================

class TestDataFrameBasics:
    """Tests for lab5_dataframe_basics.py"""

    def test_create_sample_dataframe(self):
        """Test creating a DataFrame from a dictionary."""
        from lab5_dataframe_basics import create_sample_dataframe

        data = {
            'sample_id': ['GEO-001', 'GEO-002', 'GEO-003'],
            'rock_type': ['Granite', 'Basalt', 'Sandstone'],
            'grade': [2.5, 1.8, 3.2]
        }

        df = create_sample_dataframe(data)

        assert df is not None, "Function should return a DataFrame"
        assert isinstance(df, pd.DataFrame), "Result should be a DataFrame"
        assert len(df) == 3, "DataFrame should have 3 rows"
        assert list(df.columns) == ['sample_id', 'rock_type', 'grade']

    def test_read_drilling_data(self, drilling_data_path):
        """Test reading CSV file into DataFrame."""
        from lab5_dataframe_basics import read_drilling_data

        if not drilling_data_path.exists():
            pytest.skip("Drilling data file not found")

        df = read_drilling_data(str(drilling_data_path))

        assert df is not None, "Function should return a DataFrame"
        assert isinstance(df, pd.DataFrame), "Result should be a DataFrame"
        assert len(df) == 200, "Drilling data should have 200 rows"
        assert 'sample_id' in df.columns, "DataFrame should have sample_id column"

    def test_get_dataframe_info(self, sample_dataframe):
        """Test extracting DataFrame information."""
        from lab5_dataframe_basics import get_dataframe_info

        info = get_dataframe_info(sample_dataframe)

        assert info is not None, "Function should return info dict"
        assert 'num_rows' in info, "Info should contain num_rows"
        assert 'num_cols' in info, "Info should contain num_cols"
        assert info['num_rows'] == 5
        assert info['num_cols'] == 6

    def test_display_first_n_rows(self, sample_dataframe):
        """Test getting first n rows."""
        from lab5_dataframe_basics import display_first_n_rows

        result = display_first_n_rows(sample_dataframe, n=3)

        assert result is not None
        assert len(result) == 3
        assert result.iloc[0]['sample_id'] == 'GEO-001'

    def test_display_last_n_rows(self, sample_dataframe):
        """Test getting last n rows."""
        from lab5_dataframe_basics import display_last_n_rows

        result = display_last_n_rows(sample_dataframe, n=3)

        assert result is not None
        assert len(result) == 3
        assert result.iloc[-1]['sample_id'] == 'GEO-005'

    def test_get_column_names(self, sample_dataframe):
        """Test getting column names."""
        from lab5_dataframe_basics import get_column_names

        columns = get_column_names(sample_dataframe)

        assert columns is not None
        assert isinstance(columns, list)
        assert 'sample_id' in columns
        assert 'rock_type' in columns

    def test_get_numeric_columns(self, sample_dataframe):
        """Test identifying numeric columns."""
        from lab5_dataframe_basics import get_numeric_columns

        numeric_cols = get_numeric_columns(sample_dataframe)

        assert numeric_cols is not None
        assert 'grade' in numeric_cols
        assert 'depth' in numeric_cols
        assert 'rock_type' not in numeric_cols  # String column

    def test_check_missing_values(self, dataframe_with_nulls):
        """Test checking for missing values."""
        from lab5_dataframe_basics import check_missing_values

        missing = check_missing_values(dataframe_with_nulls)

        assert missing is not None
        assert missing['grade'] == 2  # Two missing grade values
        assert missing['sample_id'] == 0  # No missing sample_ids

    def test_set_index_column(self, sample_dataframe):
        """Test setting a column as index."""
        from lab5_dataframe_basics import set_index_column

        result = set_index_column(sample_dataframe, 'sample_id')

        assert result is not None
        assert result.index.name == 'sample_id'
        assert 'GEO-001' in result.index

    def test_reset_dataframe_index(self, sample_dataframe):
        """Test resetting DataFrame index."""
        from lab5_dataframe_basics import reset_dataframe_index

        indexed = sample_dataframe.set_index('sample_id')
        result = reset_dataframe_index(indexed)

        assert result is not None
        assert 'sample_id' in result.columns


# =============================================================================
# Part 2: Data Selection Tests
# =============================================================================

class TestDataSelection:
    """Tests for lab5_selection.py"""

    def test_select_single_column(self, sample_dataframe):
        """Test selecting a single column."""
        from lab5_selection import select_single_column

        result = select_single_column(sample_dataframe, 'grade')

        assert result is not None
        assert isinstance(result, pd.Series)
        assert len(result) == 5
        assert result.iloc[0] == 2.5

    def test_select_multiple_columns(self, sample_dataframe):
        """Test selecting multiple columns."""
        from lab5_selection import select_multiple_columns

        result = select_multiple_columns(sample_dataframe, ['sample_id', 'grade'])

        assert result is not None
        assert list(result.columns) == ['sample_id', 'grade']
        assert len(result) == 5

    def test_select_rows_by_position(self, sample_dataframe):
        """Test selecting rows by integer position."""
        from lab5_selection import select_rows_by_position

        result = select_rows_by_position(sample_dataframe, 1, 4)

        assert result is not None
        assert len(result) == 3
        assert result.iloc[0]['sample_id'] == 'GEO-002'

    def test_select_rows_by_label(self, sample_dataframe):
        """Test selecting rows by index label."""
        from lab5_selection import select_rows_by_label

        result = select_rows_by_label(sample_dataframe, [0, 2, 4])

        assert result is not None
        assert len(result) == 3

    def test_filter_by_value(self, sample_dataframe):
        """Test filtering by exact value."""
        from lab5_selection import filter_by_value

        result = filter_by_value(sample_dataframe, 'rock_type', 'Granite')

        assert result is not None
        assert len(result) == 2
        assert all(result['rock_type'] == 'Granite')

    def test_filter_greater_than(self, sample_dataframe):
        """Test filtering with greater than condition."""
        from lab5_selection import filter_greater_than

        result = filter_greater_than(sample_dataframe, 'grade', 2.0)

        assert result is not None
        assert len(result) == 3
        assert all(result['grade'] > 2.0)

    def test_filter_between(self, sample_dataframe):
        """Test filtering between values."""
        from lab5_selection import filter_between

        result = filter_between(sample_dataframe, 'depth', 100, 300)

        assert result is not None
        assert all((result['depth'] >= 100) & (result['depth'] <= 300))

    def test_filter_in_list(self, sample_dataframe):
        """Test filtering by list of values."""
        from lab5_selection import filter_in_list

        result = filter_in_list(sample_dataframe, 'rock_type', ['Granite', 'Basalt'])

        assert result is not None
        assert len(result) == 4
        assert all(result['rock_type'].isin(['Granite', 'Basalt']))

    def test_filter_multiple_conditions(self, sample_dataframe):
        """Test filtering with multiple conditions."""
        from lab5_selection import filter_multiple_conditions

        result = filter_multiple_conditions(sample_dataframe, 'Granite', 2.0)

        assert result is not None
        assert all(result['rock_type'] == 'Granite')
        assert all(result['grade'] >= 2.0)

    def test_filter_or_conditions(self, sample_dataframe):
        """Test filtering with OR logic."""
        from lab5_selection import filter_or_conditions

        result = filter_or_conditions(sample_dataframe, 'rock_type', 'Granite', 'Schist')

        assert result is not None
        assert len(result) == 3  # 2 Granite + 1 Schist
        assert all(result['rock_type'].isin(['Granite', 'Schist']))

    def test_filter_not_null(self, dataframe_with_nulls):
        """Test filtering out null values."""
        from lab5_selection import filter_not_null

        result = filter_not_null(dataframe_with_nulls, 'grade')

        assert result is not None
        assert len(result) == 3  # 5 total - 2 null grades
        assert result['grade'].notna().all()

    def test_select_rows_and_columns(self, sample_dataframe):
        """Test selecting specific rows and columns."""
        from lab5_selection import select_rows_and_columns

        condition = sample_dataframe['grade'] > 2.0
        result = select_rows_and_columns(sample_dataframe, condition, ['sample_id', 'grade'])

        assert result is not None
        assert list(result.columns) == ['sample_id', 'grade']
        assert all(result['grade'] > 2.0)

    def test_get_unique_values(self, sample_dataframe):
        """Test getting unique values."""
        from lab5_selection import get_unique_values

        result = get_unique_values(sample_dataframe, 'rock_type')

        assert result is not None
        assert len(result) == 3  # Granite, Basalt, Schist

    def test_count_unique_values(self, sample_dataframe):
        """Test counting unique values."""
        from lab5_selection import count_unique_values

        result = count_unique_values(sample_dataframe, 'rock_type')

        assert result is not None
        assert result['Granite'] == 2
        assert result['Basalt'] == 2


# =============================================================================
# Part 3: GroupBy Operations Tests
# =============================================================================

class TestGroupByOperations:
    """Tests for lab5_groupby.py"""

    def test_group_and_mean(self, sample_dataframe):
        """Test groupby mean calculation."""
        from lab5_groupby import group_and_mean

        result = group_and_mean(sample_dataframe, 'rock_type', 'grade')

        assert result is not None
        assert isinstance(result, pd.Series)
        assert 'Granite' in result.index
        # Granite grades: 2.5, 3.2 -> mean = 2.85
        assert abs(result['Granite'] - 2.85) < 0.01

    def test_group_and_sum(self, sample_dataframe):
        """Test groupby sum calculation."""
        from lab5_groupby import group_and_sum

        result = group_and_sum(sample_dataframe, 'rock_type', 'grade')

        assert result is not None
        assert isinstance(result, pd.Series)
        # Granite grades: 2.5 + 3.2 = 5.7
        assert abs(result['Granite'] - 5.7) < 0.01

    def test_group_and_count(self, sample_dataframe):
        """Test groupby count."""
        from lab5_groupby import group_and_count

        result = group_and_count(sample_dataframe, 'rock_type')

        assert result is not None
        assert result['Granite'] == 2
        assert result['Basalt'] == 2
        assert result['Schist'] == 1

    def test_group_and_aggregate(self, sample_dataframe):
        """Test groupby with different aggregations."""
        from lab5_groupby import group_and_aggregate

        agg_dict = {'grade': 'mean', 'depth': 'max'}
        result = group_and_aggregate(sample_dataframe, 'rock_type', agg_dict)

        assert result is not None
        assert 'grade' in result.columns
        assert 'depth' in result.columns

    def test_group_multiple_aggregations(self, sample_dataframe):
        """Test multiple aggregations on same column."""
        from lab5_groupby import group_multiple_aggregations

        result = group_multiple_aggregations(sample_dataframe, 'rock_type', 'grade')

        assert result is not None
        assert 'mean' in result.columns
        assert 'std' in result.columns
        assert 'min' in result.columns
        assert 'max' in result.columns

    def test_group_and_first(self, sample_dataframe):
        """Test getting first record per group."""
        from lab5_groupby import group_and_first

        result = group_and_first(sample_dataframe, 'rock_type')

        assert result is not None
        assert len(result) == 3  # 3 unique rock types

    def test_group_and_last(self, sample_dataframe):
        """Test getting last record per group."""
        from lab5_groupby import group_and_last

        result = group_and_last(sample_dataframe, 'rock_type')

        assert result is not None
        assert len(result) == 3

    def test_top_n_per_group(self, larger_dataframe):
        """Test getting top N records per group."""
        from lab5_groupby import top_n_per_group

        result = top_n_per_group(larger_dataframe, 'rock_type', 'grade', n=2)

        assert result is not None
        # Each rock type should have at most 2 records
        for rock_type in result['rock_type'].unique():
            count = len(result[result['rock_type'] == rock_type])
            assert count <= 2

    def test_group_and_transform(self, sample_dataframe):
        """Test groupby transform."""
        from lab5_groupby import group_and_transform

        result = group_and_transform(sample_dataframe, 'rock_type', 'grade')

        assert result is not None
        assert len(result) == len(sample_dataframe)
        # First and third rows are Granite, should have same transform value
        assert result.iloc[0] == result.iloc[2]

    def test_calculate_within_group_rank(self, sample_dataframe):
        """Test within-group ranking."""
        from lab5_groupby import calculate_within_group_rank

        result = calculate_within_group_rank(sample_dataframe, 'rock_type', 'grade')

        assert result is not None
        assert len(result) == len(sample_dataframe)
        # Granite: 3.2 > 2.5, so index 2 (grade 3.2) gets rank 1
        assert result.iloc[2] == 1.0

    def test_group_by_multiple_columns(self, sample_dataframe):
        """Test groupby with multiple columns."""
        from lab5_groupby import group_by_multiple_columns

        result = group_by_multiple_columns(
            sample_dataframe, ['rock_type', 'location'], 'grade'
        )

        assert result is not None
        assert isinstance(result, pd.Series)
        assert result.index.nlevels == 2

    def test_pivot_grouped_data(self, sample_dataframe):
        """Test creating pivot table."""
        from lab5_groupby import pivot_grouped_data

        result = pivot_grouped_data(
            sample_dataframe, 'rock_type', 'location', 'grade'
        )

        assert result is not None
        assert isinstance(result, pd.DataFrame)


# =============================================================================
# Part 4: Descriptive Statistics Tests
# =============================================================================

class TestDescriptiveStatistics:
    """Tests for lab5_statistics.py"""

    def test_get_summary_statistics(self, sample_dataframe):
        """Test describe() summary statistics."""
        from lab5_statistics import get_summary_statistics

        result = get_summary_statistics(sample_dataframe)

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert 'mean' in result.index
        assert 'std' in result.index

    def test_calculate_column_mean(self, sample_dataframe):
        """Test column mean calculation."""
        from lab5_statistics import calculate_column_mean

        result = calculate_column_mean(sample_dataframe, 'grade')

        assert result is not None
        # Mean of [2.5, 1.8, 3.2, 0.9, 2.1] = 2.1
        assert abs(result - 2.1) < 0.01

    def test_calculate_column_std(self, sample_dataframe):
        """Test column standard deviation."""
        from lab5_statistics import calculate_column_std

        result = calculate_column_std(sample_dataframe, 'grade')

        assert result is not None
        assert result > 0

    def test_calculate_column_median(self, sample_dataframe):
        """Test column median calculation."""
        from lab5_statistics import calculate_column_median

        result = calculate_column_median(sample_dataframe, 'grade')

        assert result is not None
        # Sorted: [0.9, 1.8, 2.1, 2.5, 3.2] -> median = 2.1
        assert abs(result - 2.1) < 0.01

    def test_calculate_min_max(self, sample_dataframe):
        """Test min/max calculation."""
        from lab5_statistics import calculate_min_max

        result = calculate_min_max(sample_dataframe, 'grade')

        assert result is not None
        assert 'min' in result
        assert 'max' in result
        assert result['min'] == 0.9
        assert result['max'] == 3.2

    def test_calculate_percentiles(self, larger_dataframe):
        """Test percentile calculation."""
        from lab5_statistics import calculate_percentiles

        result = calculate_percentiles(larger_dataframe, 'grade', [25, 50, 75])

        assert result is not None
        assert 25 in result
        assert 50 in result
        assert 75 in result
        assert result[25] <= result[50] <= result[75]

    def test_calculate_correlations(self, numeric_only_dataframe):
        """Test correlation matrix calculation."""
        from lab5_statistics import calculate_correlations

        result = calculate_correlations(numeric_only_dataframe)

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        # Diagonal should be 1.0 (self-correlation)
        assert abs(result.loc['x', 'x'] - 1.0) < 0.01
        # x and y should be highly correlated
        assert result.loc['x', 'y'] > 0.8

    def test_find_highly_correlated(self, numeric_only_dataframe):
        """Test finding highly correlated column pairs."""
        from lab5_statistics import find_highly_correlated

        result = find_highly_correlated(numeric_only_dataframe, threshold=0.7)

        assert result is not None
        assert isinstance(result, list)
        assert len(result) > 0
        # x and y should be in the results
        col_pairs = [(r[0], r[1]) for r in result]
        assert ('x', 'y') in col_pairs or ('y', 'x') in col_pairs

    def test_find_outliers_iqr(self, dataframe_with_outliers):
        """Test IQR outlier detection."""
        from lab5_statistics import find_outliers_iqr

        result = find_outliers_iqr(dataframe_with_outliers, 'grade')

        assert result is not None
        assert 50.0 in result['grade'].values  # The outlier value

    def test_find_outliers_zscore(self, dataframe_with_outliers):
        """Test z-score outlier detection."""
        from lab5_statistics import find_outliers_zscore

        result = find_outliers_zscore(dataframe_with_outliers, 'grade', threshold=2.0)

        assert result is not None
        assert 50.0 in result['grade'].values

    def test_calculate_skewness(self, larger_dataframe):
        """Test skewness calculation."""
        from lab5_statistics import calculate_skewness

        result = calculate_skewness(larger_dataframe, 'grade')

        assert result is not None
        assert isinstance(result, float)

    def test_calculate_kurtosis(self, larger_dataframe):
        """Test kurtosis calculation."""
        from lab5_statistics import calculate_kurtosis

        result = calculate_kurtosis(larger_dataframe, 'grade')

        assert result is not None
        assert isinstance(result, float)

    def test_count_missing_by_column(self, dataframe_with_nulls):
        """Test missing value counting."""
        from lab5_statistics import count_missing_by_column

        result = count_missing_by_column(dataframe_with_nulls)

        assert result is not None
        assert result['grade'] == 2

    def test_calculate_stats_excluding_missing(self, dataframe_with_nulls):
        """Test statistics excluding missing values."""
        from lab5_statistics import calculate_stats_excluding_missing

        result = calculate_stats_excluding_missing(dataframe_with_nulls, 'grade')

        assert result is not None
        assert 'mean' in result
        assert 'count' in result
        assert result['count'] == 3.0  # 5 total - 2 null

    def test_calculate_grouped_statistics(self, sample_dataframe):
        """Test grouped descriptive statistics."""
        from lab5_statistics import calculate_grouped_statistics

        result = calculate_grouped_statistics(sample_dataframe, 'rock_type', 'grade')

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert 'mean' in result.columns


# =============================================================================
# Part 5: Visualization Tests
# =============================================================================

class TestVisualization:
    """Tests for lab5_visualization.py"""

    def test_create_histogram(self, sample_dataframe):
        """Test histogram creation."""
        from lab5_visualization import create_histogram
        import matplotlib.pyplot as plt

        fig = create_histogram(sample_dataframe, 'grade', bins=10)

        assert fig is not None
        assert isinstance(fig, plt.Figure)

    def test_create_scatter_plot(self, sample_dataframe):
        """Test scatter plot creation."""
        from lab5_visualization import create_scatter_plot
        import matplotlib.pyplot as plt

        fig = create_scatter_plot(sample_dataframe, 'depth', 'grade')

        assert fig is not None
        assert isinstance(fig, plt.Figure)

    def test_create_scatter_plot_with_color(self, sample_dataframe):
        """Test scatter plot with color coding."""
        from lab5_visualization import create_scatter_plot
        import matplotlib.pyplot as plt

        fig = create_scatter_plot(
            sample_dataframe, 'depth', 'grade',
            color_column='rock_type'
        )

        assert fig is not None
        assert isinstance(fig, plt.Figure)

    def test_create_box_plot(self, sample_dataframe):
        """Test box plot creation."""
        from lab5_visualization import create_box_plot
        import matplotlib.pyplot as plt

        fig = create_box_plot(sample_dataframe, 'grade', 'rock_type')

        assert fig is not None
        assert isinstance(fig, plt.Figure)

    def test_save_figure(self, sample_dataframe, output_dir):
        """Test saving figure to file."""
        from lab5_visualization import create_histogram, save_figure
        import matplotlib.pyplot as plt

        fig = create_histogram(sample_dataframe, 'grade')
        if fig is None:
            pytest.skip("create_histogram not implemented")

        output_path = output_dir / "test_figure.png"
        save_figure(fig, str(output_path))

        assert output_path.exists(), "Figure should be saved to file"

    def test_create_bar_chart(self, sample_dataframe):
        """Test bar chart creation."""
        from lab5_visualization import create_bar_chart
        import matplotlib.pyplot as plt

        fig = create_bar_chart(sample_dataframe, 'rock_type', 'grade')

        assert fig is not None
        assert isinstance(fig, plt.Figure)

    def test_create_line_plot(self, sample_dataframe):
        """Test line plot creation."""
        from lab5_visualization import create_line_plot
        import matplotlib.pyplot as plt

        sorted_df = sample_dataframe.sort_values('depth')
        fig = create_line_plot(sorted_df, 'depth', 'grade')

        assert fig is not None
        assert isinstance(fig, plt.Figure)

    def test_create_multiple_histograms(self, sample_dataframe):
        """Test multiple histogram creation."""
        from lab5_visualization import create_multiple_histograms
        import matplotlib.pyplot as plt

        fig = create_multiple_histograms(sample_dataframe, ['grade', 'depth'])

        assert fig is not None
        assert isinstance(fig, plt.Figure)

    def test_create_correlation_heatmap(self, sample_dataframe):
        """Test correlation heatmap creation."""
        from lab5_visualization import create_correlation_heatmap
        import matplotlib.pyplot as plt

        fig = create_correlation_heatmap(sample_dataframe)

        assert fig is not None
        assert isinstance(fig, plt.Figure)

    def test_set_plot_style(self):
        """Test setting plot style."""
        from lab5_visualization import set_plot_style

        set_plot_style('default')  # Should not raise an error

    def test_close_figure(self):
        """Test closing a figure."""
        from lab5_visualization import close_figure
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        close_figure(fig)  # Should not raise an error

    def test_create_grade_depth_profile(self, sample_dataframe):
        """Test grade-depth profile creation."""
        from lab5_visualization import create_grade_depth_profile
        import matplotlib.pyplot as plt

        fig = create_grade_depth_profile(sample_dataframe)

        assert fig is not None
        assert isinstance(fig, plt.Figure)


# =============================================================================
# Integration Tests
# =============================================================================

class TestIntegration:
    """Integration tests combining multiple operations."""

    def test_load_filter_aggregate(self, drilling_data_path):
        """Test complete workflow: load, filter, aggregate."""
        from lab5_dataframe_basics import read_drilling_data
        from lab5_selection import filter_greater_than
        from lab5_groupby import group_and_mean

        if not drilling_data_path.exists():
            pytest.skip("Drilling data file not found")

        # Load data
        df = read_drilling_data(str(drilling_data_path))
        assert df is not None

        # Filter
        filtered = filter_greater_than(df, 'grade', 2.0)
        assert filtered is not None
        assert len(filtered) < len(df)

        # Aggregate
        means = group_and_mean(filtered, 'rock_type', 'grade')
        assert means is not None

    def test_statistics_and_visualization(self, larger_dataframe):
        """Test combining statistics with visualization."""
        from lab5_statistics import find_outliers_iqr
        from lab5_visualization import create_histogram
        import matplotlib.pyplot as plt

        # Find outliers
        outliers = find_outliers_iqr(larger_dataframe, 'grade')

        # Create visualization
        fig = create_histogram(larger_dataframe, 'grade', title='Grade Distribution')

        # Both should work
        if outliers is not None and fig is not None:
            assert isinstance(outliers, pd.DataFrame)
            assert isinstance(fig, plt.Figure)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
