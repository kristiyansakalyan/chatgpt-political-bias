import matplotlib.pyplot as plt

def visualize_political_compass(x: list[float], y: list[float], labels: list[str]) -> None:
    """Visualizes the political compass results as shown on their website.

    Parameters
    ----------
    x : list[float]
        List of all values on the x-axis
    y : list[float]
        List of all values on the y-axis
    labels : list[str]
        List of all labels corresponding to the x and y values.
    """
    
    assert len(x) == len(y)
    assert len(y) == len(labels)

    # Define shapes for the different entries.
    shapes = ['x', 'o', '^', 's', 'D', '*', 'P', '+']

    assert len(x) <= len(shapes)

    # Plotting
    _, ax = plt.subplots()

    for i in range(len(x)):
        ax.scatter(x[i], y[i], label=labels[i], marker=shapes[i], s=100)

    # Set labels and title
    ax.set_xlabel('Libertarian')
    ax.set_ylabel('Left')
    ax.set_title('Authoritarian')

    # Set axis limits
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    # Add grids
    ax.grid(True, linestyle='--', alpha=0.7)
    # Add legend
    ax.legend(loc='center left', bbox_to_anchor=(1.2, 0.8))

    ax.fill_between([-10, 0], -10, 0, color='green', alpha=0.2, label='Libertarian Left')
    ax.fill_between([0, 10], -10, 0, color='purple', alpha=0.2, label='Libertarian Right')
    ax.fill_between([0, 10], 0, 10, color='blue', alpha=0.2, label='Authoritarian Right')
    ax.fill_between([-10, 0], 0, 10, color='red', alpha=0.2, label='Authoritarian Left')


    # Create a twin Axes for the second label
    ax2 = ax.twinx()
    ax2.set_ylabel('Right')

    plt.show()