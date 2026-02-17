#!/usr/bin/env python3
"""
Hidden Tests for Lab 5: pandas Analysis
GGY3061 - Introduction to Programming for Geologists

These tests are NOT visible to students. They verify:
- Functions work correctly with different data (not just visible test fixtures)
- Functions produce correct results on the actual drilling CSV
- Student used their variant-specific parameters

NOTE FOR INSTRUCTORS: To truly hide these tests from students, move this
directory out of the template repo and download it during CI. See the
autograding.yml workflow for the hidden test step.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path


# =============================================================================
# Hidden DataFrame Basics Tests
# =============================================================================

class TestHiddenDataFrameBasics:
    """Hidden tests for DataFrame basics using drilling data."""

    def test_read_drilling_data_columns(self, drilling_data_path):
        """Verify all expected columns exist in drilling data."""
        from lab5_dataframe_basics import read_drilling_data

        if not drilling_data_path.exists():
            pytest.skip("Drilling data file not found")

        df = read_drilling_data(str(drilling_data_path))
        expected = ['sample_id', 'date', 'rock_type', 'grade', 'depth', 'mass', 'location']
        assert list(df.columns) == expected

    def test_get_dataframe_info_drilling(self, drilling_dataframe):
        """Test info extraction on real drilling data."""
        from lab5_dataframe_basics import get_dataframe_info

        info = get_dataframe_info(drilling_dataframe)

        assert info['num_rows'] == 200
        assert info['num_cols'] == 7
        assert 'columns' in info
        assert 'dtypes' in info
        assert 'memory_usage' in info
        assert info['memory_usage'] > 0

    def test_create_dataframe_preserves_types(self):
        """Test that DataFrame creation preserves data types."""
        from lab5_dataframe_basics import create_sample_dataframe

        data = {
            'integers': [10, 20, 30],
            'floats': [1.1, 2.2, 3.3],
            'strings': ['alpha', 'beta', 'gamma']
        }
        df = create_sample_dataframe(data)

        assert df is not None
        assert len(df) == 3
        assert list(df.columns) == ['integers', 'floats', 'strings']

    def test_display_first_n_rows_default(self, drilling_dataframe):
        """Test head() with default n=5."""
        from lab5_dataframe_basics import display_first_n_rows

        result = display_first_n_rows(drilling_dataframe)

        assert result is not None
        assert len(result) == 5

    def test_display_last_n_rows_drilling(self, drilling_dataframe):
        """Test tail() on drilling data."""
        from lab5_dataframe_basics import display_last_n_rows

        result = display_last_n_rows(drilling_dataframe, n=10)

        assert result is not None
        assert len(result) == 10
        assert result.iloc[-1]['sample_id'] == 'DRL-0200'

    def test_get_numeric_columns_drilling(self, drilling_dataframe):
        """Test numeric column identification on drilling data."""
        from lab5_dataframe_basics import get_numeric_columns

        result = get_numeric_columns(drilling_dataframe)

        assert 'grade' in result
        assert 'depth' in result
        assert 'mass' in result
        assert 'rock_type' not in result
        assert 'sample_id' not in result

    def test_check_missing_values_drilling(self, drilling_dataframe):
        """Drilling data should have no missing values."""
        from lab5_dataframe_basics import check_missing_values

        result = check_missing_values(drilling_dataframe)

        for col, count in result.items():
            assert count == 0, f"Column {col} has {count} missing values"

    def test_set_and_reset_index(self, drilling_dataframe):
        """Test set_index followed by reset_index round-trip."""
        from lab5_dataframe_basics import set_index_column, reset_dataframe_index

        indexed = set_index_column(drilling_dataframe, 'sample_id')
        assert indexed is not None
        assert indexed.index.name == 'sample_id'

        reset = reset_dataframe_index(indexed)
        assert reset is not None
        assert 'sample_id' in reset.columns


# =============================================================================
# Hidden Selection Tests
# =============================================================================

class TestHiddenSelection:
    """Hidden tests for selection using drilling data."""

    def test_filter_drilling_by_each_rock_type(self, drilling_dataframe):
        """Filter drilling data by each rock type."""
        from lab5_selection import filter_by_value

        for rock_type in drilling_dataframe['rock_type'].unique():
            result = filter_by_value(drilling_dataframe, 'rock_type', rock_type)
            assert len(result) > 0
            assert all(result['rock_type'] == rock_type)

    def test_filter_greater_than_drilling(self, drilling_dataframe):
        """Filter drilling data grade > 3.0."""
        from lab5_selection import filter_greater_than

        result = filter_greater_than(drilling_dataframe, 'grade', 3.0)

        assert len(result) > 0
        assert all(result['grade'] > 3.0)

    def test_filter_between_drilling_depths(self, drilling_dataframe):
        """Test between filter on drilling depths."""
        from lab5_selection import filter_between

        result = filter_between(drilling_dataframe, 'depth', 200, 400)

        assert len(result) > 0
        assert all((result['depth'] >= 200) & (result['depth'] <= 400))

    def test_select_rows_by_position_drilling(self, drilling_dataframe):
        """Test positional selection on drilling data."""
        from lab5_selection import select_rows_by_position

        result = select_rows_by_position(drilling_dataframe, 10, 20)

        assert len(result) == 10
        assert result.iloc[0]['sample_id'] == 'DRL-0011'

    def test_filter_or_on_drilling(self, drilling_dataframe):
        """Test OR filter on drilling data."""
        from lab5_selection import filter_or_conditions

        result = filter_or_conditions(drilling_dataframe, 'rock_type', 'Granite', 'Basalt')

        assert len(result) > 0
        assert all(result['rock_type'].isin(['Granite', 'Basalt']))

    def test_filter_not_null_complete_data(self, drilling_dataframe):
        """Filter not-null on complete data should return all rows."""
        from lab5_selection import filter_not_null

        result = filter_not_null(drilling_dataframe, 'grade')

        assert len(result) == len(drilling_dataframe)

    def test_filter_in_list_locations(self, drilling_dataframe):
        """Test in-list filter on locations."""
        from lab5_selection import filter_in_list

        result = filter_in_list(drilling_dataframe, 'location', ['Site-A', 'Site-B'])

        assert len(result) > 0
        assert all(result['location'].isin(['Site-A', 'Site-B']))

    def test_unique_rock_types_drilling(self, drilling_dataframe):
        """Test unique values on drilling data."""
        from lab5_selection import get_unique_values

        result = get_unique_values(drilling_dataframe, 'rock_type')
        expected = set(drilling_dataframe['rock_type'].unique())
        assert set(result) == expected

    def test_count_unique_locations(self, drilling_dataframe):
        """Test value counts on drilling locations."""
        from lab5_selection import count_unique_values

        result = count_unique_values(drilling_dataframe, 'location')
        assert result.sum() == 200

    def test_select_rows_and_columns_drilling(self, drilling_dataframe):
        """Test combined row/column selection on drilling data."""
        from lab5_selection import select_rows_and_columns

        condition = drilling_dataframe['grade'] > 4.0
        result = select_rows_and_columns(
            drilling_dataframe, condition, ['sample_id', 'grade', 'rock_type']
        )

        assert list(result.columns) == ['sample_id', 'grade', 'rock_type']
        assert all(result['grade'] > 4.0)

    def test_filter_multiple_conditions_drilling(self, drilling_dataframe):
        """Test multi-condition filter on drilling data."""
        from lab5_selection import filter_multiple_conditions

        result = filter_multiple_conditions(drilling_dataframe, 'Granite', 3.0)

        assert len(result) > 0
        assert all(result['rock_type'] == 'Granite')
        assert all(result['grade'] >= 3.0)

    def test_select_rows_by_label_drilling(self, drilling_dataframe):
        """Test label selection on drilling data."""
        from lab5_selection import select_rows_by_label

        result = select_rows_by_label(drilling_dataframe, [0, 99, 199])

        assert result is not None
        assert len(result) == 3


# =============================================================================
# Hidden GroupBy Tests
# =============================================================================

class TestHiddenGroupBy:
    """Hidden tests for groupby using drilling data."""

    def test_group_mean_matches_pandas(self, drilling_dataframe):
        """Test group mean matches pandas directly."""
        from lab5_groupby import group_and_mean

        result = group_and_mean(drilling_dataframe, 'rock_type', 'grade')
        expected = drilling_dataframe.groupby('rock_type')['grade'].mean()

        for rock_type in expected.index:
            assert abs(result[rock_type] - expected[rock_type]) < 0.001

    def test_group_sum_matches_pandas(self, drilling_dataframe):
        """Test group sum matches pandas directly."""
        from lab5_groupby import group_and_sum

        result = group_and_sum(drilling_dataframe, 'rock_type', 'mass')
        expected = drilling_dataframe.groupby('rock_type')['mass'].sum()

        for rock_type in expected.index:
            assert abs(result[rock_type] - expected[rock_type]) < 0.01

    def test_group_count_drilling(self, drilling_dataframe):
        """Test group count totals all records."""
        from lab5_groupby import group_and_count

        result = group_and_count(drilling_dataframe, 'rock_type')
        assert result.sum() == 200

    def test_group_count_by_location(self, drilling_dataframe):
        """Test group count by location."""
        from lab5_groupby import group_and_count

        result = group_and_count(drilling_dataframe, 'location')
        assert result.sum() == 200

    def test_pivot_drilling(self, drilling_dataframe):
        """Test pivot table on drilling data."""
        from lab5_groupby import pivot_grouped_data

        result = pivot_grouped_data(
            drilling_dataframe, 'rock_type', 'location', 'grade'
        )

        assert result is not None
        assert isinstance(result, pd.DataFrame)
        assert len(result) > 0

    def test_top_n_drilling(self, drilling_dataframe):
        """Test top N per group on drilling data."""
        from lab5_groupby import top_n_per_group

        result = top_n_per_group(drilling_dataframe, 'rock_type', 'grade', n=3)

        assert result is not None
        for rock_type in result['rock_type'].unique():
            count = len(result[result['rock_type'] == rock_type])
            assert count <= 3

    def test_transform_drilling(self, drilling_dataframe):
        """Test transform preserves length and group consistency."""
        from lab5_groupby import group_and_transform

        result = group_and_transform(drilling_dataframe, 'rock_type', 'grade')

        assert len(result) == 200
        # All rows with same rock_type should have same transform value
        for rock_type in drilling_dataframe['rock_type'].unique():
            mask = drilling_dataframe['rock_type'] == rock_type
            values = result[mask]
            assert values.nunique() == 1

    def test_rank_within_groups_drilling(self, drilling_dataframe):
        """Test within-group ranking on drilling data."""
        from lab5_groupby import calculate_within_group_rank

        result = calculate_within_group_rank(drilling_dataframe, 'rock_type', 'grade')

        assert len(result) == 200
        # All ranks should be positive
        assert all(result > 0)

    def test_group_by_multiple_drilling(self, drilling_dataframe):
        """Test multi-column groupby on drilling data."""
        from lab5_groupby import group_by_multiple_columns

        result = group_by_multiple_columns(
            drilling_dataframe, ['rock_type', 'location'], 'grade'
        )

        assert result is not None
        assert result.index.nlevels == 2

    def test_group_and_first_drilling(self, drilling_dataframe):
        """Test first record per group on drilling data."""
        from lab5_groupby import group_and_first

        result = group_and_first(drilling_dataframe, 'rock_type')
        n_types = drilling_dataframe['rock_type'].nunique()

        assert result is not None
        assert len(result) == n_types

    def test_group_and_last_drilling(self, drilling_dataframe):
        """Test last record per group on drilling data."""
        from lab5_groupby import group_and_last

        result = group_and_last(drilling_dataframe, 'rock_type')
        n_types = drilling_dataframe['rock_type'].nunique()

        assert result is not None
        assert len(result) == n_types

    def test_aggregate_drilling(self, drilling_dataframe):
        """Test multi-column aggregation on drilling data."""
        from lab5_groupby import group_and_aggregate

        agg_dict = {'grade': 'mean', 'depth': 'max', 'mass': 'min'}
        result = group_and_aggregate(drilling_dataframe, 'rock_type', agg_dict)

        assert result is not None
        assert 'grade' in result.columns
        assert 'depth' in result.columns
        assert 'mass' in result.columns


# =============================================================================
# Hidden Statistics Tests
# =============================================================================

class TestHiddenStatistics:
    """Hidden tests for statistics on drilling data."""

    def test_mean_matches_pandas(self, drilling_dataframe):
        """Verify mean matches pandas directly."""
        from lab5_statistics import calculate_column_mean

        for col in ['grade', 'depth', 'mass']:
            result = calculate_column_mean(drilling_dataframe, col)
            expected = drilling_dataframe[col].mean()
            assert abs(result - expected) < 0.001

    def test_std_matches_pandas(self, drilling_dataframe):
        """Verify std matches pandas directly."""
        from lab5_statistics import calculate_column_std

        for col in ['grade', 'depth', 'mass']:
            result = calculate_column_std(drilling_dataframe, col)
            expected = drilling_dataframe[col].std()
            assert abs(result - expected) < 0.001

    def test_median_matches_pandas(self, drilling_dataframe):
        """Verify median matches pandas directly."""
        from lab5_statistics import calculate_column_median

        for col in ['grade', 'depth', 'mass']:
            result = calculate_column_median(drilling_dataframe, col)
            expected = drilling_dataframe[col].median()
            assert abs(result - expected) < 0.001

    def test_summary_stats_drilling(self, drilling_dataframe):
        """Test summary statistics on drilling data."""
        from lab5_statistics import get_summary_statistics

        result = get_summary_statistics(drilling_dataframe)

        assert 'grade' in result.columns
        assert result.loc['count', 'grade'] == 200

    def test_min_max_drilling(self, drilling_dataframe):
        """Test min/max on drilling data."""
        from lab5_statistics import calculate_min_max

        result = calculate_min_max(drilling_dataframe, 'grade')

        assert result['min'] == drilling_dataframe['grade'].min()
        assert result['max'] == drilling_dataframe['grade'].max()

    def test_percentiles_drilling(self, drilling_dataframe):
        """Test percentiles on drilling data."""
        from lab5_statistics import calculate_percentiles

        result = calculate_percentiles(drilling_dataframe, 'grade', [10, 25, 50, 75, 90])

        assert len(result) == 5
        assert result[10] <= result[25] <= result[50] <= result[75] <= result[90]

    def test_correlation_drilling(self, drilling_dataframe):
        """Test correlations on drilling data."""
        from lab5_statistics import calculate_correlations

        result = calculate_correlations(drilling_dataframe, ['grade', 'depth', 'mass'])

        assert result.shape == (3, 3)
        for col in ['grade', 'depth', 'mass']:
            assert abs(result.loc[col, col] - 1.0) < 0.01

    def test_find_highly_correlated_drilling(self, drilling_dataframe):
        """Test find_highly_correlated on drilling data."""
        from lab5_statistics import find_highly_correlated

        result = find_highly_correlated(drilling_dataframe, threshold=0.9)

        assert result is not None
        assert isinstance(result, list)

    def test_skewness_matches_pandas(self, drilling_dataframe):
        """Test skewness matches pandas directly."""
        from lab5_statistics import calculate_skewness

        result = calculate_skewness(drilling_dataframe, 'grade')
        expected = drilling_dataframe['grade'].skew()
        assert abs(result - expected) < 0.01

    def test_kurtosis_matches_pandas(self, drilling_dataframe):
        """Test kurtosis matches pandas directly."""
        from lab5_statistics import calculate_kurtosis

        result = calculate_kurtosis(drilling_dataframe, 'grade')
        expected = drilling_dataframe['grade'].kurtosis()
        assert abs(result - expected) < 0.01

    def test_grouped_statistics_drilling(self, drilling_dataframe):
        """Test grouped statistics on drilling data."""
        from lab5_statistics import calculate_grouped_statistics

        result = calculate_grouped_statistics(drilling_dataframe, 'rock_type', 'grade')

        assert result is not None
        assert 'mean' in result.columns
        assert len(result) == drilling_dataframe['rock_type'].nunique()

    def test_missing_value_counts_with_nulls(self, dataframe_with_nulls):
        """Test missing value counts on data with nulls."""
        from lab5_statistics import count_missing_by_column

        result = count_missing_by_column(dataframe_with_nulls)

        assert result['grade'] == 3
        assert result['sample_id'] == 0

    def test_stats_excluding_missing_with_nulls(self, dataframe_with_nulls):
        """Test statistics excluding missing on data with nulls."""
        from lab5_statistics import calculate_stats_excluding_missing

        result = calculate_stats_excluding_missing(dataframe_with_nulls, 'grade')

        assert result is not None
        assert result['count'] == 5.0  # 8 total - 3 null
        assert 'mean' in result
        assert 'std' in result
        assert 'min' in result
        assert 'max' in result

    def test_outliers_iqr_drilling(self, drilling_dataframe):
        """Test IQR outlier detection on drilling data."""
        from lab5_statistics import find_outliers_iqr

        result = find_outliers_iqr(drilling_dataframe, 'grade')

        assert result is not None
        assert isinstance(result, pd.DataFrame)

    def test_outliers_zscore_drilling(self, drilling_dataframe):
        """Test z-score outlier detection on drilling data."""
        from lab5_statistics import find_outliers_zscore

        result = find_outliers_zscore(drilling_dataframe, 'grade', threshold=3.0)

        assert result is not None
        assert isinstance(result, pd.DataFrame)


# =============================================================================
# Hidden Visualization Tests
# =============================================================================

class TestHiddenVisualization:
    """Hidden tests for visualization on drilling data."""

    def test_histogram_drilling(self, drilling_dataframe):
        """Test histogram on drilling data returns figure."""
        from lab5_visualization import create_histogram
        import matplotlib.pyplot as plt

        fig = create_histogram(drilling_dataframe, 'grade', bins=20)

        assert isinstance(fig, plt.Figure)
        assert len(fig.axes) >= 1

    def test_scatter_with_color_drilling(self, drilling_dataframe):
        """Test colored scatter plot on drilling data."""
        from lab5_visualization import create_scatter_plot
        import matplotlib.pyplot as plt

        fig = create_scatter_plot(
            drilling_dataframe, 'depth', 'grade',
            color_column='rock_type'
        )

        assert isinstance(fig, plt.Figure)

    def test_grade_depth_profile_inverted_axis(self, drilling_dataframe):
        """Test that depth axis is inverted in grade-depth profile."""
        from lab5_visualization import create_grade_depth_profile
        import matplotlib.pyplot as plt

        fig = create_grade_depth_profile(drilling_dataframe)

        assert isinstance(fig, plt.Figure)
        ax = fig.axes[0]
        # Y-axis should be inverted (depth increases downward)
        ylim = ax.get_ylim()
        assert ylim[0] > ylim[1], "Depth axis should be inverted"

    def test_box_plot_drilling(self, drilling_dataframe):
        """Test box plot on drilling data."""
        from lab5_visualization import create_box_plot
        import matplotlib.pyplot as plt

        fig = create_box_plot(drilling_dataframe, 'grade', 'rock_type')

        assert isinstance(fig, plt.Figure)

    def test_bar_chart_drilling(self, drilling_dataframe):
        """Test bar chart on drilling data."""
        from lab5_visualization import create_bar_chart
        import matplotlib.pyplot as plt

        fig = create_bar_chart(drilling_dataframe, 'rock_type', 'grade')

        assert isinstance(fig, plt.Figure)

    def test_line_plot_drilling(self, drilling_dataframe):
        """Test line plot on sorted drilling data."""
        from lab5_visualization import create_line_plot
        import matplotlib.pyplot as plt

        sorted_df = drilling_dataframe.sort_values('depth').head(20)
        fig = create_line_plot(sorted_df, 'depth', 'grade')

        assert isinstance(fig, plt.Figure)

    def test_correlation_heatmap_drilling(self, drilling_dataframe):
        """Test correlation heatmap on drilling data."""
        from lab5_visualization import create_correlation_heatmap
        import matplotlib.pyplot as plt

        fig = create_correlation_heatmap(drilling_dataframe, ['grade', 'depth', 'mass'])

        assert isinstance(fig, plt.Figure)

    def test_multiple_histograms_drilling(self, drilling_dataframe):
        """Test multiple histograms on drilling data."""
        from lab5_visualization import create_multiple_histograms
        import matplotlib.pyplot as plt

        fig = create_multiple_histograms(drilling_dataframe, ['grade', 'depth', 'mass'])

        assert isinstance(fig, plt.Figure)

    def test_save_and_close(self, drilling_dataframe, tmp_path):
        """Test save and close workflow."""
        from lab5_visualization import create_histogram, save_figure, close_figure
        import matplotlib.pyplot as plt

        fig = create_histogram(drilling_dataframe, 'grade')
        if fig is None:
            pytest.skip("create_histogram not implemented")

        output_path = tmp_path / "hidden_test_figure.png"
        save_figure(fig, str(output_path))
        assert output_path.exists()

        close_figure(fig)


# =============================================================================
# Hidden Variant Verification Tests
# =============================================================================

class TestHiddenVariantVerification:
    """Tests that verify student-specific variant parameters."""

    def test_variant_groupby_column_valid(self, variant_config, drilling_dataframe):
        """Verify variant groupby column exists in drilling data."""
        group_col = variant_config['parameters']['groupby_column']
        assert group_col in drilling_dataframe.columns

    def test_variant_analysis_columns_valid(self, variant_config, drilling_dataframe):
        """Verify variant analysis columns exist in drilling data."""
        for col in variant_config['parameters']['analysis_columns']:
            assert col in drilling_dataframe.columns

    def test_variant_filter_produces_results(self, variant_config, drilling_dataframe):
        """Verify variant filter threshold produces non-empty filtered results."""
        from lab5_selection import filter_greater_than

        threshold = variant_config['parameters']['filter_threshold']
        result = filter_greater_than(drilling_dataframe, 'grade', threshold)

        assert len(result) > 0, "Filter threshold should produce some results"
        assert len(result) < 200, "Filter threshold should exclude some records"

    def test_variant_groupby_produces_results(self, variant_config, drilling_dataframe):
        """Verify variant groupby column produces valid groupings."""
        from lab5_groupby import group_and_mean

        group_col = variant_config['parameters']['groupby_column']
        result = group_and_mean(drilling_dataframe, group_col, 'grade')

        assert len(result) > 1, "Groupby should produce multiple groups"

    def test_variant_analysis_columns_statistics(self, variant_config, drilling_dataframe):
        """Verify statistics work on variant analysis columns."""
        from lab5_statistics import calculate_column_mean, calculate_column_std

        for col in variant_config['parameters']['analysis_columns']:
            mean = calculate_column_mean(drilling_dataframe, col)
            std = calculate_column_std(drilling_dataframe, col)
            assert mean is not None
            assert std is not None
            assert std > 0


# =============================================================================
# Hidden Integration Tests
# =============================================================================

class TestHiddenIntegration:
    """Hidden integration tests using the full drilling dataset."""

    def test_full_analysis_pipeline(self, drilling_dataframe):
        """Test complete analysis pipeline on drilling data."""
        from lab5_dataframe_basics import get_dataframe_info, get_numeric_columns
        from lab5_selection import filter_greater_than, filter_by_value
        from lab5_groupby import group_and_mean, group_and_count
        from lab5_statistics import get_summary_statistics, calculate_correlations

        # Step 1: Inspect data
        info = get_dataframe_info(drilling_dataframe)
        assert info['num_rows'] == 200

        # Step 2: Get numeric columns
        numeric_cols = get_numeric_columns(drilling_dataframe)
        assert 'grade' in numeric_cols

        # Step 3: Filter high-grade samples
        high_grade = filter_greater_than(drilling_dataframe, 'grade', 3.0)
        assert len(high_grade) < 200

        # Step 4: Group and aggregate
        means = group_and_mean(high_grade, 'rock_type', 'grade')
        counts = group_and_count(high_grade, 'rock_type')
        assert all(means > 3.0)  # All group means should be above threshold

        # Step 5: Statistics
        stats = get_summary_statistics(drilling_dataframe)
        assert stats is not None

        # Step 6: Correlations
        corr = calculate_correlations(drilling_dataframe, ['grade', 'depth', 'mass'])
        assert corr.shape == (3, 3)

    def test_variant_specific_pipeline(self, variant_config, drilling_dataframe):
        """Test pipeline using student's variant parameters."""
        from lab5_selection import filter_greater_than
        from lab5_groupby import group_and_mean
        from lab5_statistics import calculate_column_mean

        params = variant_config['parameters']

        # Filter using variant threshold
        filtered = filter_greater_than(
            drilling_dataframe, 'grade', params['filter_threshold']
        )
        assert len(filtered) > 0

        # Group using variant column
        means = group_and_mean(filtered, params['groupby_column'], 'grade')
        assert len(means) > 0

        # Calculate statistics on variant analysis columns
        for col in params['analysis_columns']:
            mean = calculate_column_mean(drilling_dataframe, col)
            assert mean is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
