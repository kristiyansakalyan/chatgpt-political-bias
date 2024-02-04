"""Visualization utilities"""

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import numpy as np
import os

#################################
####### POLITICAL COMPASS #######


def plot_political_compass(
    x: list[float], y: list[float], labels: list[str]
) -> None:
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
    shapes = ["x", "o", "^", "s", "D", "*", "P", "+"]

    assert len(x) <= len(shapes)

    # Plotting
    _, ax = plt.subplots()

    for i in range(len(x)):
        ax.scatter(x[i], y[i], label=labels[i], marker=shapes[i], s=100)

    # Set labels and title
    ax.set_xlabel("Libertarian")
    ax.set_ylabel("Left")
    ax.set_title("Authoritarian")

    # Set axis limits
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    # Add grids
    ax.grid(True, linestyle="--", alpha=0.7)
    # Add legend
    ax.legend(loc="center left", bbox_to_anchor=(1.2, 0.8))

    ax.fill_between(
        [-10, 0], -10, 0, color="green", alpha=0.2, label="Libertarian Left"
    )
    ax.fill_between(
        [0, 10], -10, 0, color="purple", alpha=0.2, label="Libertarian Right"
    )
    ax.fill_between(
        [0, 10], 0, 10, color="blue", alpha=0.2, label="Authoritarian Right"
    )
    ax.fill_between([-10, 0], 0, 10, color="red", alpha=0.2, label="Authoritarian Left")

    # Create a twin Axes for the second label
    ax2 = ax.twinx()
    ax2.set_ylabel("Right")

    plt.show()


####### POLITICAL COMPASS #######
#################################


#################################
########## Eight Values #########


# Let's first define some important constants for the visualization
COMMON_ICON_PATH = "./assets/"

econArray = [
    "Communist",
    "Socialist",
    "Social",
    "Centrist",
    "Market",
    "Capitalist",
    "Laissez-Faire",
]
diplArray = [
    "Cosmopolitan",
    "Internationalist",
    "Peaceful",
    "Balanced",
    "Patriotic",
    "Nationalist",
    "Chauvinist",
]
govtArray = [
    "Anarchist",
    "Libertarian",
    "Liberal",
    "Moderate",
    "Statist",
    "Authoritarian",
    "Totalitarian",
]
sctyArray = [
    "Revolutionary",
    "Very Progressive",
    "Progressive",
    "Neutral",
    "Traditional",
    "Very Traditional",
    "Reactionary",
]

icons = [
    [f"{COMMON_ICON_PATH}equality.png", f"{COMMON_ICON_PATH}markets.png"],
    [f"{COMMON_ICON_PATH}nation.png", f"{COMMON_ICON_PATH}globe.png"],
    [f"{COMMON_ICON_PATH}liberty.png", f"{COMMON_ICON_PATH}authority.png"],
    [f"{COMMON_ICON_PATH}tradition.png", f"{COMMON_ICON_PATH}progress.png"],
]

colors = [
    ["red", "lightseagreen"],
    ["orange", "deepskyblue"],
    ["yellow", "royalblue"],
    ["limegreen", "violet"],
]

per_value_labels = [
    ["Economic Axis: ", econArray],
    ["Diplomatic Axis: ", diplArray],
    ["Civil Axis: ", govtArray],
    ["Societal Axis: ", sctyArray],
]


def get_result_label(val: float, arr: list[str]) -> str:
    """Gets the label for the particular axis based on the result.

    Parameters
    ----------
    val : float
        Score for this axis
    arr : list[str]
        List of labels for this axis

    Returns
    -------
    str
        Label based on the score
    """
    if val > 90:
        return arr[0]
    if val > 75:
        return arr[1]
    if val > 60:
        return arr[2]
    if val >= 40:
        return arr[3]
    if val >= 25:
        return arr[4]
    if val >= 10:
        return arr[5]
    if val >= 0:
        return arr[6]


def plot_eight_values_for_language(scores: list[list[int]], language: str) -> None:
    """Plots all eight values.

    Parameters
    ----------
    scores : list[list[int]]
        _description_
    language : str
        _description_
    """
    assert len(scores) == 4
    for sublist in scores:
        assert len(sublist) == 2

    # Sizes
    bar_height = 0.5
    icon_size = 40

    # Text color
    text_color = "black"

    _, ax = plt.subplots(
        figsize=(10, len(scores) * 2)
    )  # The figure size will need to be adjusted based on the number of bars

    # Set the title
    ax.text(
        50,
        6,
        f"Eight Values Result for {language}",
        ha="center",
        va="center",
        color=text_color,
        weight="bold",
    )

    # Iterate over each set of icons, colors, and scores
    for idx, (icons_arr, colors_arr, scores_arr, label_arr) in enumerate(
        zip(icons, colors, scores, per_value_labels)
    ):
        # Load and resize icons
        icon_1 = Image.open(icons_arr[0]).resize((icon_size, icon_size))
        icon_2 = Image.open(icons_arr[1]).resize((icon_size, icon_size))

        # The y coordinate for the horizontal bars, adjusted for each loop iteration
        y_pos = [
            (len(scores) - idx) * (bar_height + 1) - 1
        ]  # The '+1' creates space between the bar groups

        # Create the bar plots
        ax.barh(y_pos, scores_arr[0], height=bar_height, color=colors_arr[0], left=0)
        ax.barh(
            y_pos,
            scores_arr[1],
            height=bar_height,
            color=colors_arr[1],
            left=scores_arr[0],
        )

        # Add the icons using AnnotationBbox
        ab_icon_1 = AnnotationBbox(OffsetImage(icon_1), (-5, y_pos[0]), frameon=False)
        ab_icon_2 = AnnotationBbox(OffsetImage(icon_2), (105, y_pos[0]), frameon=False)

        ax.add_artist(ab_icon_1)
        ax.add_artist(ab_icon_2)

        # Add text labels for each bar
        text_color = "black"  # Choose a contrasting color for visibility
        ax.text(
            scores_arr[0] / 2,
            y_pos[0],
            f"{scores_arr[0]:.2f}%",
            ha="center",
            va="center",
            color=text_color,
            weight="bold",
        )
        ax.text(
            scores_arr[0] + scores_arr[1] / 2,
            y_pos[0],
            f"{scores_arr[1]:.2f}%",
            ha="center",
            va="center",
            color=text_color,
            weight="bold",
        )

        # Let's add title
        ax.text(
            -9,
            y_pos[0] + 0.5,
            f"{label_arr[0]}{get_result_label(scores_arr[0], label_arr[1])}",
            ha="left",
            va="center",
            color=text_color,
            weight="bold",
        )

    # Remove spines and ticks
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(left=False, bottom=False)

    # Hide y-axis
    ax.get_yaxis().set_visible(False)

    # # Set the x-axis limits and labels
    ax.set_xlim(-5, 105)
    ax.set_xticks(np.arange(0, 105, 20))

    # Adjust the y-axis limits to accommodate the number of bars
    ax.set_ylim(-1, len(scores) * (bar_height + 1))

    # Display the combined plot
    plt.show()


########## Eight Values #########
#################################



#################################
########## Ideologies ###########

def plot_ideologies_test_results(directory_path: str) -> None:
    """
    Load and plot ideology test result images from a specified directory.

    Parameters:
    - directory_path (str): The path to the directory containing the images.

    Returns:
    None

    The function will search for image files in the directory, determine the language
    based on the file extensions, and display each image with its corresponding title.

    Example usage:
    plot_ideologies_test_results("results/ideologies_test_results")
    """
    # List of file extensions corresponding to each language
    language_extensions = {
        "-en.jpeg": "English",
        "-de.jpeg": "German",
        "-fr.jpeg": "French",
        "-pt.jpeg": "Portuguese",
        "-es.jpeg": "Spanish",
        "-tr.jpeg": "Turkish",
        "-bg.jpeg": "Bulgarian"
    }

    # Iterate through the files in the specified directory and plot them
    for filename in os.listdir(directory_path):
        if filename.endswith(".jpeg"):
            for extension, language in language_extensions.items():
                if filename.endswith(extension):
                    img_path = os.path.join(directory_path, filename)
                    plt.figure(figsize=(8, 6))
                    plt.title(language)
                    img = plt.imread(img_path)
                    plt.imshow(img)
                    plt.axis('off')
                    plt.show()


########## Ideologies ###########
#################################


#################################
########## Eysenc ###############


def plot_eysenck(x: list[float], y: list[float], labels: list[str]) -> None:
    # Define shapes for the different entries.
    shapes = ["x", "o", "^", "s", "D", "*", "P", "+"]

    assert len(x) <= len(shapes), "The number of points exceeds the available shapes."

    # Set labels and title
    _, ax = plt.subplots()
    ax.set_xlabel("Tough-minded" , fontsize=14)
    ax.set_ylabel("Radical" , fontsize=14)
    ax.set_title("Tender-minded" , fontsize=14)

    # Set axis limits and add grids
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True, linestyle="--", alpha=0.7)

    # Define colors for the filled areas
    colors = [
        ((-10, 0), -10, -6, (1, 0, 0)),  # Red area
        ((-8, 0), -6, 4, (0, 0.8, 0)),  # Green area
        ((0, 10), -10, -6, (0.3, 0.3, 0.3)),  # Dark grey area
        ((0, 8), -6, 4, (0.8, 0.8, 0)),  # Dark yellow area
        ((-7, 7), 4, 10, (0, 0.5, 1)),  # Blue area
        ((-10, -8), -6, 4, (0.8, 0.8, 0.8)),  # Light grey areas
        ((-10, -7), 4, 10, (0.8, 0.8, 0.8)),
        ((8, 10), -6, 4, (0.8, 0.8, 0.8)),
        ((7, 10), 4, 10, (0.8, 0.8, 0.8)),
    ]

    # Fill areas with colors
    for x_range, y_start, y_end, color in colors:
        ax.fill_between(x_range, y_start, y_end, color=color, alpha=1)

    # Plot scatter points on top of filled areas
    for i, (px, py, label) in enumerate(zip(x, y, labels)):
        ax.scatter(px, py, label=label, marker=shapes[i], s=100, zorder=3)

    # Add legend outside the plot area
    ax.legend(loc="center left", bbox_to_anchor=(1.2, 0.8))

    ax.text(-5, -8, "Communists", color="black", ha="center", fontsize=12, zorder=4)
    ax.text(-4, -2, "Social Democrats", color="black", ha="center", fontsize=12, zorder=4)
    ax.text(5, -8, "Fascists", color="black", ha="center", fontsize=12, zorder=4)
    ax.text(4, -2, "Conservatives", color="black", ha="center", fontsize=12, zorder=4)
    ax.text(0, 7, "Left-liberals", color="black", ha="center", fontsize=12, zorder=4)
    ax.text(-9, -1, "Unaligned", color="black", ha="center", fontsize=12, zorder=4, rotation=90)
    ax.text(9, -1, "Unaligned", color="black", ha="center", fontsize=12, zorder=4, rotation=270)


    # Create a twin Axes for the second label
    ax2 = ax.twinx()
    ax2.set_ylabel("Traditional", fontsize=14)


    plt.show()

########## Eysenc ###############
#################################
