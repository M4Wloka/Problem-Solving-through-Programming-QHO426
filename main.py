"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
# --------------------- Import all from all of the files --------------------- #
from exporter import save_data_to_txt, save_data_to_json, save_data_to_csv
from process import row_number_process, check_same_choice, submenu_a_view_reviews_by_park_initialization, submenu_b_averages_by_the_month_process, choice_of_the_park_input, submenu_a_view_reviews_by_park_visual_choice, submenu_a_view_reviews_by_park_display_reviews, submenu_a_numbers_of_reviews_by_park_and_reviewer_location_initialization, submenu_a_numbers_of_reviews_by_park_and_reviewer_location_visual_choice, submenu_a_average_score_per_year_by_park_initialization, submenu_a_averages_by_the_month_process, submenu_b_most_reviewed_parks, submenu_b_average_review_of_each_park, submenu_b_top_10_countries_averages, submenu_a_average_score_per_year_by_park_visual_choice
from tui import submenu_a_choice_confirmation, submenu_b_choice_confirmation, submenu_c_choice_confirmation, submenu_choice, welcome
from visual import plot_bar_chart, submenu_b_average_review_of_each_park_chart_bar, submenu_b_averages_by_the_month_visual, submenu_b_most_reviewed_parks_bars

# ---------------------------------------------------------------------------- #


# - to make any program flow I put the definitions with my appreciated queue - #
def main():
    # ------------------------- welcome message with --- ------------------------- #
    welcome()
    # ------------------------ number of the rows display ------------------------ #
    row_number_process()
    # ---------------------------------------------------------------------------- #

    while True:
        # ----------------------- obtain user choice from menu ----------------------- #
        final_choice_main_menu = check_same_choice()
        submenu_user_choice = submenu_choice()
        # --------------- confirm user choice with confirmation message -------------- #

        # ---------------------------------------------------------------------------- #
        #                                 menu option A                                #
        # ---------------------------------------------------------------------------- #
        if final_choice_main_menu == "a":
            if submenu_user_choice == "a":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_a_choice_confirmation(submenu_user_choice)
                # ------------------------- call sumbenu A-A options ------------------------- #
                process_submenu_a_a()
                # ---------------------------------------------------------------------------- #
            elif submenu_user_choice == "b":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_a_choice_confirmation(submenu_user_choice)
                # ------------------------- call sumbenu A-B options ------------------------- #
                process_submenu_a_b()
                # ---------------------------------------------------------------------------- #
            elif submenu_user_choice == "c":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_a_choice_confirmation(submenu_user_choice)
                # ------------------------- call sumbenu A-C options ------------------------- #
                process_submenu_a_c()
                # ---------------------------------------------------------------------------- #
            elif submenu_user_choice == "d":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_a_choice_confirmation(submenu_user_choice)
                # ------------------------- call sumbenu A-D options ------------------------- #
                process_sumbenu_a_d()
                # ---------------------------------------------------------------------------- #

        # ---------------------------------------------------------------------------- #
        #                                B menu options                                #
        # ---------------------------------------------------------------------------- #
        elif final_choice_main_menu == "b":
            if submenu_user_choice == "a":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_b_choice_confirmation(submenu_user_choice)
                # ------------------------- call sumbenu B-A options ------------------------- #
                process_submenu_b_a()
                # ---------------------------------------------------------------------------- #
            elif submenu_user_choice == "b":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_b_choice_confirmation(submenu_user_choice)
                # ------------------------- call sumbenu B-B options ------------------------- #
                process_submenu_b_b()
                # ---------------------------------------------------------------------------- #
            elif submenu_user_choice == "c":
                submenu_b_choice_confirmation(submenu_user_choice)
                # ------------------------- call sumbenu B-C options ------------------------- #
                process_submenu_b_c()
                # ---------------------------------------------------------------------------- #
            elif submenu_user_choice == "d":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_b_choice_confirmation(submenu_user_choice)
                park_names = [
                    "Disneyland_California",
                    "Disneyland_HongKong",
                    "Disneyland_Paris",
                ]

                averages, selected_park = submenu_b_averages_by_the_month_process(
                    park_names
                )
                submenu_b_averages_by_the_month_visual(averages, selected_park)
                # ---------------------------------------------------------------------------- #

        # ---------------------------------------------------------------------------- #
        #                                C menu options                                #
        # ---------------------------------------------------------------------------- #
        # ------ class menu option/ everything connected with export and saving ------ #
        # ----- in the csv, txt, json files every single operation connected with ---- #
        # --------------------- this class is in exporter.py file -------------------- #
        # ---------------------------------------------------------------------------- #
        elif final_choice_main_menu == "c":
            if submenu_user_choice == "a":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_c_choice_confirmation(submenu_user_choice)
                # ------------- final definition to exporter file to save in json ------------ #
                save_data_to_json()
                # ---------------------------------------------------------------------------- #
            elif submenu_user_choice == "b":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_c_choice_confirmation(submenu_user_choice)
                # ------------ final definition from exporter file to save in csv ------------ #
                save_data_to_csv()
                # ---------------------------------------------------------------------------- #
            elif submenu_user_choice == "c":
                # --------------------------- submenu confirmation --------------------------- #
                submenu_c_choice_confirmation(submenu_user_choice)
                # ------------- final definition from exporter file to save in txt ------------ #
                save_data_to_txt()
                # ---------------------------------------------------------------------------- #

        # ---------------------------------------------------------------------------- #
        #                                 X menu options                                #
        # ---------------------------------------------------------------------------- #
        # ------------ this is last menu function do not need confirmation ----------- #
        # ----------------------------- it is exit option ---------------------------- #
        elif final_choice_main_menu == "x":
            break
        # ---------------------------------------------------------------------------- #


# -------------- definition which call functions from process.py ------------- #
def process_submenu_a_a():
    park_names = submenu_a_view_reviews_by_park_initialization()
    selected_park = choice_of_the_park_input(park_names)
    selected_reviews = submenu_a_view_reviews_by_park_visual_choice(selected_park)
    submenu_a_view_reviews_by_park_display_reviews(selected_reviews)


# -------------- definition which call functions from process.py ------------- #
def process_submenu_a_b():
    sorted_user_localizations = (
        submenu_a_numbers_of_reviews_by_park_and_reviewer_location_initialization()
    )
    park_names = submenu_a_view_reviews_by_park_initialization()
    selected_park = choice_of_the_park_input(park_names)
    submenu_a_numbers_of_reviews_by_park_and_reviewer_location_visual_choice(
        sorted_user_localizations, selected_park
    )


# -------------- definition which call functions from process.py ------------- #
def process_submenu_a_c():
    sorted_user_year = submenu_a_average_score_per_year_by_park_initialization()
    park_names = submenu_a_view_reviews_by_park_initialization()
    selected_park = choice_of_the_park_input(park_names)
    submenu_a_average_score_per_year_by_park_visual_choice(
        sorted_user_year, selected_park
    )


# -------------- definition which call functions from process.py ------------- #
def process_sumbenu_a_d():
    sorted_user_localizations = (
        submenu_a_numbers_of_reviews_by_park_and_reviewer_location_initialization()
    )
    park_names = submenu_a_view_reviews_by_park_initialization()
    submenu_a_averages_by_the_month_process(sorted_user_localizations, park_names)


# ------------ definition which call functions from process.py and ----------- #
# -------------- definition which call functions from visual.py -------------- #
def process_submenu_b_a():
    parks_names, review_counts = submenu_b_most_reviewed_parks()
    submenu_b_most_reviewed_parks_bars(parks_names, review_counts)


# ------------ definition which call functions from process.py and ----------- #
# -------------- definition which call functions from visual.py -------------- #
def process_submenu_b_b():
    submenu_b_average_review_of_each_park()
    submenu_b_average_review_of_each_park_chart_bar()


# ------------ definition which call functions from process.py and ----------- #
# -------------- definition which call functions from visual.py -------------- #
def process_submenu_b_c():
    park_names = submenu_a_view_reviews_by_park_initialization()
    selected_park = choice_of_the_park_input(park_names)
    top_countries, avg_ratings = submenu_b_top_10_countries_averages(selected_park)
    plot_bar_chart(top_countries, avg_ratings, selected_park)


# ---------------------------------------------------------------------------- #
# --------- I had to use this option because I am using visual studio -------- #
# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    main()
