import matplotlib.pyplot as plt
import numpy as np


def create_colored_plane(
    xmin=-10,
    xmax=10,
    ymin=-10,
    ymax=10,
    step=2,
    bg_color="#FFFFFF",
    axis_color="#000000",
    grid_color="#CCCCCC"
):
    """
    Generates a Cartesian plane with customizable colors.

    Parameters
    ----------
    xmin, xmax : int
        X-axis limits.
    ymin, ymax : int
        Y-axis limits.
    step : int
        Tick spacing.
    bg_color : str
        Background color.
    axis_color : str
        Color of the x- and y-axes.
    grid_color : str
        Color of the gridlines.
    """

    fig, ax = plt.subplots(figsize=(8, 8))

    # Set background color
    ax.set_facecolor(bg_color)
    fig.patch.set_facecolor(bg_color)

    # Set axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Move axes to the origin
    ax.spines["left"].set_position("zero")
    ax.spines["left"].set_color(axis_color)
    ax.spines["left"].set_linewidth(1.5)

    ax.spines["bottom"].set_position("zero")
    ax.spines["bottom"].set_color(axis_color)
    ax.spines["bottom"].set_linewidth(1.5)

    # Hide outer borders
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    # Ticks
    ax.tick_params(colors=axis_color, labelsize=9)
    ax.set_xticks(np.arange(xmin, xmax + 1, step))
    ax.set_yticks(np.arange(ymin, ymax + 1, step))

    # Grid
    ax.grid(
        True,
        which="both",
        linestyle="--",
        color=grid_color,
        alpha=0.7
    )

    return fig, ax