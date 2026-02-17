#!/usr/bin/env python3
"""
Lab 5: Basic Visualization
GGY3061 - Introduction to Programming for Geologists

This module covers data visualization with pandas and matplotlib:
- Histograms for distribution analysis
- Scatter plots for relationships
- Box plots for comparing groups
- Saving figures to files

Learning Outcome: LO5.5 - Create basic visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional, List, Tuple
from pathlib import Path


def create_histogram(df: pd.DataFrame,
                     column: str,
                     bins: int = 20,
                     title: Optional[str] = None,
                     xlabel: Optional[str] = None,
                     ylabel: str = "Frequency") -> plt.Figure:
    """
    Create a histogram for a numeric column.

    Args:
        df: Input DataFrame
        column: Column to plot
        bins: Number of bins (default 20)
        title: Plot title (default: "Distribution of {column}")
        xlabel: X-axis label (default: column name)
        ylabel: Y-axis label (default: "Frequency")

    Returns:
        matplotlib Figure object

    Example:
        >>> df = pd.DataFrame({'grade': [1, 2, 2, 3, 3, 3, 4, 4, 5]})
        >>> fig = create_histogram(df, 'grade', bins=5)
        >>> fig is not None
        True
    """
    # TODO: Create a histogram
    # Hints:
    # 1. Create figure: fig, ax = plt.subplots(figsize=(10, 6))
    # 2. Plot histogram: df[column].hist(bins=bins, ax=ax, edgecolor='black')
    # 3. Set title: ax.set_title(title or f"Distribution of {column}")
    # 4. Set labels: ax.set_xlabel(), ax.set_ylabel()
    # 5. Return fig
    pass


def create_scatter_plot(df: pd.DataFrame,
                        x_column: str,
                        y_column: str,
                        color_column: Optional[str] = None,
                        title: Optional[str] = None,
                        xlabel: Optional[str] = None,
                        ylabel: Optional[str] = None) -> plt.Figure:
    """
    Create a scatter plot showing relationship between two columns.

    Args:
        df: Input DataFrame
        x_column: Column for x-axis
        y_column: Column for y-axis
        color_column: Optional column for color coding points
        title: Plot title
        xlabel: X-axis label (default: x_column)
        ylabel: Y-axis label (default: y_column)

    Returns:
        matplotlib Figure object

    Example:
        >>> df = pd.DataFrame({
        ...     'depth': [100, 200, 300],
        ...     'grade': [2.0, 3.0, 1.5]
        ... })
        >>> fig = create_scatter_plot(df, 'depth', 'grade')
        >>> fig is not None
        True
    """
    # TODO: Create a scatter plot
    # Hints:
    # 1. Create figure: fig, ax = plt.subplots(figsize=(10, 6))
    # 2. If color_column:
    #    - Get unique values and create a colormap
    #    - Plot each group with different color
    # 3. Else: ax.scatter(df[x_column], df[y_column])
    # 4. Set title and labels
    # 5. Add legend if color_column
    # 6. Return fig
    pass


def create_box_plot(df: pd.DataFrame,
                    value_column: str,
                    group_column: str,
                    title: Optional[str] = None,
                    xlabel: Optional[str] = None,
                    ylabel: Optional[str] = None) -> plt.Figure:
    """
    Create a box plot comparing distributions across groups.

    Args:
        df: Input DataFrame
        value_column: Numeric column for values
        group_column: Categorical column for groups
        title: Plot title
        xlabel: X-axis label (default: group_column)
        ylabel: Y-axis label (default: value_column)

    Returns:
        matplotlib Figure object

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt', 'Basalt'],
        ...     'grade': [2.0, 3.0, 1.5, 2.5]
        ... })
        >>> fig = create_box_plot(df, 'grade', 'rock_type')
        >>> fig is not None
        True
    """
    # TODO: Create a box plot
    # Hints:
    # 1. Create figure: fig, ax = plt.subplots(figsize=(10, 6))
    # 2. Use df.boxplot(column=value_column, by=group_column, ax=ax)
    # 3. Set title and labels
    # 4. Remove automatic title from boxplot: plt.suptitle('')
    # 5. Return fig
    pass


def create_bar_chart(df: pd.DataFrame,
                     category_column: str,
                     value_column: str,
                     title: Optional[str] = None,
                     xlabel: Optional[str] = None,
                     ylabel: Optional[str] = None) -> plt.Figure:
    """
    Create a bar chart showing values for each category.

    The values should be aggregated (mean) by category.

    Args:
        df: Input DataFrame
        category_column: Column for categories (x-axis)
        value_column: Numeric column for values (y-axis)
        title: Plot title
        xlabel: X-axis label (default: category_column)
        ylabel: Y-axis label (default: value_column)

    Returns:
        matplotlib Figure object

    Example:
        >>> df = pd.DataFrame({
        ...     'rock_type': ['Granite', 'Granite', 'Basalt', 'Basalt'],
        ...     'grade': [2.0, 3.0, 1.5, 2.5]
        ... })
        >>> fig = create_bar_chart(df, 'rock_type', 'grade')
        >>> fig is not None
        True
    """
    # TODO: Create a bar chart
    # Hints:
    # 1. Calculate means: means = df.groupby(category_column)[value_column].mean()
    # 2. Create figure: fig, ax = plt.subplots(figsize=(10, 6))
    # 3. Plot bars: means.plot(kind='bar', ax=ax)
    # 4. Set title and labels
    # 5. Rotate x-tick labels if needed: plt.xticks(rotation=45)
    # 6. Return fig
    pass


def create_line_plot(df: pd.DataFrame,
                     x_column: str,
                     y_column: str,
                     title: Optional[str] = None,
                     xlabel: Optional[str] = None,
                     ylabel: Optional[str] = None,
                     marker: str = 'o') -> plt.Figure:
    """
    Create a line plot.

    Args:
        df: Input DataFrame (should be sorted by x_column)
        x_column: Column for x-axis
        y_column: Column for y-axis
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        marker: Marker style (default 'o')

    Returns:
        matplotlib Figure object

    Example:
        >>> df = pd.DataFrame({
        ...     'depth': [0, 100, 200, 300],
        ...     'grade': [0.5, 1.5, 2.0, 1.8]
        ... })
        >>> fig = create_line_plot(df, 'depth', 'grade')
        >>> fig is not None
        True
    """
    # TODO: Create a line plot
    # Hints:
    # 1. Create figure: fig, ax = plt.subplots(figsize=(10, 6))
    # 2. Plot line: ax.plot(df[x_column], df[y_column], marker=marker)
    # 3. Set title and labels
    # 4. Add grid: ax.grid(True, alpha=0.3)
    # 5. Return fig
    pass


def create_multiple_histograms(df: pd.DataFrame,
                                columns: List[str],
                                bins: int = 20) -> plt.Figure:
    """
    Create multiple histograms in a single figure.

    Args:
        df: Input DataFrame
        columns: List of columns to plot
        bins: Number of bins for each histogram

    Returns:
        matplotlib Figure object with subplots

    Example:
        >>> df = pd.DataFrame({
        ...     'grade': [1, 2, 3, 4, 5],
        ...     'depth': [100, 200, 300, 400, 500]
        ... })
        >>> fig = create_multiple_histograms(df, ['grade', 'depth'])
        >>> fig is not None
        True
    """
    # TODO: Create multiple histograms
    # Hints:
    # 1. Calculate grid size (e.g., 2 columns)
    # 2. Create subplots: fig, axes = plt.subplots(nrows, ncols, figsize=...)
    # 3. Flatten axes if needed: axes = axes.flatten()
    # 4. Loop through columns and plot each histogram
    # 5. Hide unused subplots
    # 6. Use fig.tight_layout()
    # 7. Return fig
    pass


def create_correlation_heatmap(df: pd.DataFrame,
                                columns: Optional[List[str]] = None,
                                title: str = "Correlation Matrix") -> plt.Figure:
    """
    Create a heatmap of correlations between numeric columns.

    Args:
        df: Input DataFrame
        columns: Optional list of columns (uses all numeric if None)
        title: Plot title

    Returns:
        matplotlib Figure object

    Example:
        >>> df = pd.DataFrame({
        ...     'a': [1, 2, 3, 4, 5],
        ...     'b': [2, 4, 6, 8, 10],
        ...     'c': [5, 4, 3, 2, 1]
        ... })
        >>> fig = create_correlation_heatmap(df)
        >>> fig is not None
        True
    """
    # TODO: Create correlation heatmap
    # Hints:
    # 1. Select numeric columns if not specified
    # 2. Calculate correlation: corr = df[columns].corr()
    # 3. Create figure: fig, ax = plt.subplots(figsize=(10, 8))
    # 4. Use ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
    # 5. Add colorbar: plt.colorbar(im, ax=ax)
    # 6. Set tick labels: ax.set_xticks, ax.set_xticklabels, etc.
    # 7. Optionally add correlation values as text
    # 8. Return fig
    pass


def save_figure(fig: plt.Figure,
                filepath: str,
                dpi: int = 150,
                bbox_inches: str = 'tight') -> None:
    """
    Save a matplotlib figure to a file.

    Args:
        fig: Figure to save
        filepath: Output file path (supports .png, .pdf, .svg)
        dpi: Resolution in dots per inch (default 150)
        bbox_inches: Bounding box ('tight' removes whitespace)

    Example:
        >>> fig, ax = plt.subplots()
        >>> ax.plot([1, 2, 3])
        [<matplotlib.lines.Line2D ...>]
        >>> save_figure(fig, 'test_plot.png')
    """
    # TODO: Save the figure
    # Hint: Use fig.savefig(filepath, dpi=dpi, bbox_inches=bbox_inches)
    pass


def close_figure(fig: plt.Figure) -> None:
    """
    Close a figure to free memory.

    Args:
        fig: Figure to close
    """
    # TODO: Close the figure
    # Hint: Use plt.close(fig)
    pass


def set_plot_style(style: str = 'seaborn-v0_8-whitegrid') -> None:
    """
    Set the matplotlib plot style.

    Args:
        style: Style name (e.g., 'seaborn-v0_8-whitegrid', 'ggplot', 'default')

    Common styles:
        - 'seaborn-v0_8-whitegrid': Clean with grid lines
        - 'ggplot': R-like style
        - 'default': Matplotlib default
    """
    # TODO: Set the plot style
    # Hint: Use plt.style.use(style)
    pass


def create_grade_depth_profile(df: pd.DataFrame,
                                depth_column: str = 'depth',
                                grade_column: str = 'grade',
                                title: str = "Grade vs Depth Profile") -> plt.Figure:
    """
    Create a geological grade-depth profile plot.

    This is a common visualization in mining geology showing how
    grade varies with depth. Depth is typically on y-axis (inverted).

    Args:
        df: Input DataFrame
        depth_column: Column with depth values
        grade_column: Column with grade values
        title: Plot title

    Returns:
        matplotlib Figure object

    Example:
        >>> df = pd.DataFrame({
        ...     'depth': [0, 100, 200, 300],
        ...     'grade': [0.5, 2.0, 3.0, 1.5]
        ... })
        >>> fig = create_grade_depth_profile(df, 'depth', 'grade')
        >>> fig is not None
        True
    """
    # TODO: Create a grade-depth profile
    # Hints:
    # 1. Create figure: fig, ax = plt.subplots(figsize=(8, 10))
    # 2. Plot: ax.scatter(df[grade_column], df[depth_column])
    # 3. Invert y-axis: ax.invert_yaxis()
    # 4. Set labels: Grade on x-axis, Depth on y-axis
    # 5. Add grid
    # 6. Return fig
    pass


# =============================================================================
# Main execution for testing
# =============================================================================

if __name__ == "__main__":
    # Test your implementations here
    import numpy as np

    print("Testing Visualization Functions...")

    # Create test data
    np.random.seed(42)
    test_df = pd.DataFrame({
        'sample_id': [f'GEO-{i:03d}' for i in range(1, 101)],
        'rock_type': np.random.choice(['Granite', 'Basalt', 'Schist'], 100),
        'grade': np.random.exponential(2, 100),
        'depth': np.random.normal(300, 100, 100),
        'mass': np.random.uniform(10, 25, 100)
    })

    print("Test DataFrame created with", len(test_df), "records")

    # Test create_histogram
    fig = create_histogram(test_df, 'grade', bins=15, title='Grade Distribution')
    if fig is not None:
        save_figure(fig, 'test_histogram.png')
        print("Histogram created and saved")
        close_figure(fig)
    else:
        print("create_histogram not implemented yet")

    # Test create_scatter_plot
    fig = create_scatter_plot(test_df, 'depth', 'grade', color_column='rock_type')
    if fig is not None:
        save_figure(fig, 'test_scatter.png')
        print("Scatter plot created and saved")
        close_figure(fig)
    else:
        print("create_scatter_plot not implemented yet")

    # Test create_box_plot
    fig = create_box_plot(test_df, 'grade', 'rock_type')
    if fig is not None:
        save_figure(fig, 'test_boxplot.png')
        print("Box plot created and saved")
        close_figure(fig)
    else:
        print("create_box_plot not implemented yet")

    print("\nVisualization module tests complete.")
    print("Check the generated .png files to verify plots.")
