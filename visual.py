"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt

from process import (
    submenu_b_average_review_of_each_park,
)


# ---------------------------------------------------------------------------- #
#                             ----- Section C -----                            #
# ---------------------------------------------------------------------------- #


# -----10. The first sub-menu B option should display a pie chart showing ---- #
# --------------- the number of reviews-each park has received. --------------- #
# ---------------------------------------------------------------------------- #
# ---------------------------- [B] Visualise Data ---------------------------- #
# -------------------------- [A] Most Reviewed Parks ------------------------- #
# ---------------------------------------------------------------------------- #
# ------------------- definition for displaying pie-chart ------------------- #
def submenu_b_most_reviewed_parks_bars(parks_names, review_counts):
    # -------------------- labels for names and reviews count -------------------- #
    labels = [
        f"{parks_names[0]}\n reviews: {review_counts[0]}",
        f"{parks_names[1]}\n reviews: {review_counts[1]}",
        f"{parks_names[2]}\n reviews: {review_counts[2]}",
    ]

    fig, ax = plt.subplots()
    # ----------------------------- sizes and labels ----------------------------- #
    ax.pie(review_counts, labels=labels, hatch=["**O", "oO", "O.O", ".||."])
    # ----------------------- hatch for different patterns ----------------------- #
    plt.show()


# -------- 11. The second sub-menu option should present the average r ------- #
# -------------- review scores for each park a single bar chart ------------- #
# ---------------------------------------------------------------------------- #
# ---------------------------- [B] Visualise Data ---------------------------- #
# ---------------------------- [B] Average Scores ---------------------------- #
# ---------------------------------------------------------------------------- #
def submenu_b_average_review_of_each_park_chart_bar():
    # ----------------------- import averages from process ----------------------- #
    (
        average_california,
        average_hong_kong,
        average_paris,
    ) = submenu_b_average_review_of_each_park()
    fig, ax = plt.subplots()
    # ----------------------- list for park names formatted ----------------------- #
    parks_names = [
        "Disneyland California ",
        "Disneyland Hong-Kong",
        "Disneyland Paris",
    ]
    # ---------------------------- list with averages ---------------------------- #
    park_averages = [average_california, average_hong_kong, average_paris]
    # ---------------------------- colors of the bars ---------------------------- #
    bar_colors = ["tab:red", "tab:blue", "tab:green"]
    # ----------------------------- side description ----------------------------- #
    bar_labels = [
        f"Disneyland California = {average_california}",
        f"Disneyland Hong-Kong = {average_hong_kong}",
        f"Disneyland Paris = {average_paris}",
    ]

    ax.bar(parks_names, park_averages, label=bar_labels, color=bar_colors)

    ax.set_ylabel("Marks")
    ax.set_title("Disneyland averages")
    ax.legend(title="Rounded average review for each Disneyland")

    plt.show()


# ----- 12. The third sub-menu option will ask the user to enter a park. ----- #
# ------ It will then display a barchart that shows the top 10 locations ----- #

# ---------------------------------------------------------------------------- #
# ---------------------------- [B] Visualise Data ---------------------------- #
# ---------------------- [C] Park Ranking by Nationality --------------------- #
# ---------------------------------------------------------------------------- #


# ---------------- I made decision to do the easiest bar-chart --------------- #
def plot_bar_chart(countries, averages, selected_park):
    plt.bar(countries, averages.values())
    # ---------------- if to just make correct naming on bar-chart --------------- #
    if selected_park == "Disneyland_California":
        plt.title("Disneyland California reviews")
    elif selected_park == "Disneyland_HongKong":
        plt.title("Disneyland Hong-Kong reviews")
    elif selected_park == "Disneyland_Paris":
        plt.title("Disneyland Paris reviews")

    plt.xticks(rotation=45)
    plt.show()


# ----- 13. The final sub-menu option will ask the user to enter a park. ----- #
# ------ It will then display a bar chart that shows the average rating ------ #
# -------------- that park received for each month of the year. -------------- #
# ---------- You do not need to worry about the year for this task, ---------- #
# ------- so May 2018 and May 2019 will both be simply counted as May. ------- #
# ----------------- The bar chart should be ordered by month. ---------------- #
# --------- The final output should be a bar chart with the months of -------- #
# ----- the year (in order) along-the X axis and the average rating on the ---- #
# ---------------------------------- Y axis. --------------------------------- #


# ---------------------------------------------------------------------------- #
# ---------------------------- [B] Visualise Data ---------------------------- #
# -------------------- [D] Most Popular per Month by Park -------------------- #
# ---------------------------------------------------------------------------- #
def submenu_b_averages_by_the_month_visual(averages, selected_park):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    plt.bar(months, averages)

    if selected_park == "Disneyland_California":
        plt.title("Disneyland California reviews")
    elif selected_park == "Disneyland_HongKong":
        plt.title("Disneyland Hong-Kong reviews")
    elif selected_park == "Disneyland_Paris":
        plt.title("Disneyland Paris reviews")

    plt.xticks(rotation=45)
    plt.show()
