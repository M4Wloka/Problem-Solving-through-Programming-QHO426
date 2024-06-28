"""
This module is responsible for processing the data.  It will largely contain functions that will receive the overall
dataset and perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv
from tui import (
    row_number_display,
    main_menu_options_display,
    main_menu_input,
    menu_choice_confirmation,
    graphical_ascii_art,
    choice_a,
    choice_b,
    graphical_ascii_wrong_input,
    print_argument,
    choice_input,
    choice_of_the_park_input,
    choice_c,
)


# ------------------- global variable with path of the file ------------------ #
file_path = "data/disneyland_reviews.csv"


# ----- this function opening the file/ it is clear code organization ----- #
def open_park_data():
    csvfile = open(file_path, newline="")
    disneyland_parks = csv.reader(csvfile)
    next(disneyland_parks)
    # ------------------- skip header because we don't need it ------------------- #
    return disneyland_parks, csvfile


# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#                             ----- Section A -----                            #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
# -------------- 2. Read in the data from the provided CSV file, ------------- # +
# ------------- said data should be stored in a list. The program ------------ #
# -------------- should confirm to the user when it has finished ------------- #
# -------------------------- reading in the dataset. ------------------------- #
# -------------- It should also tell the user how many rows are -------------- #
# ------------------------------ in the dataset. ----------------------------- #
# ---------------------------------------------------------------------------- #
def row_number_process():
    # -------------------------- read the data from csv -------------------------- #
    disneyland_parks, file = open_park_data()
    # ----------- checking rows number by changing the csv to the list ----------- #
    rows_nb = len(list(disneyland_parks))
    # ---------------- saying the user how many rows are in the dataset --------------- #
    file.close()
    # ---------------------------- close the csv file ---------------------------- #
    row_number_display(rows_nb)
    # -------------- call the function which is printing row number -------------- #
    # ----------------------------- function from tui ---------------------------- #


# ---------------------------------------------------------------------------- #
# ------------------5. The program should run continuously. ------------------- #
# --------- Once the user has entered their choice, it should confirm -------- #
# --------------- this choice and then display the menu again, --------------- #
# ------------------- asking the user for their selection. ------------------- #
# -------------------- Be careful how you implement this, -------------------- #
# ---------- the program does not need to display the title and load --------- #
# ------- in the dataset again. The program should only end if the user ------ #
# ------------ indicates they wish to exit the program through the ----------- #
# ------------------------- appropriate menu choice. ------------------------- #
# ---------------------------------------------------------------------------- #
# ------------------ function with approval of the choice ------------------ #
def check_same_choice():
    while True:
        # -------- calling main menu option because there I have there display ------- #
        # -------------------------- of main menu (A,B,C,D) -------------------------- #
        main_menu_options_display()
        # ------------ I wanted to use my variable in the input and choice ----------- #
        # ----------------- and challenging (approval) of main menu ---------------- #
        final_choice_main_menu = main_menu_input()
        # ----- menu choice confirmation is a definition which will be displayed, ----- #
        # ------------------ for example after clicking a or b, or x ----------------- #
        # ------------------------ displaying approval of it ----------------------- #
        menu_choice_confirmation(final_choice_main_menu)

        if final_choice_main_menu == "a":
            # --------- this function is a big letters to double-click the letter -------- #
            graphical_ascii_art()
            # --------- display second time a main menu to see a choice for user --------- #
            main_menu_options_display()
            # --------------- again after first input we have second input --------------- #
            final_choice_main_menu = input().lower()
            if final_choice_main_menu == "a":
                # ----- if another choice is the same as first print submenu A choices ----- #
                choice_a()
                # ------------- I used break because continuation wil be in main ------------- #
                break

        elif final_choice_main_menu == "b":
            # --------- this function is a big letters to double-click the letter -------- #
            graphical_ascii_art()
            # --------- display second time a main menu to see a choice for user --------- #
            main_menu_options_display()
            # --------------- again after first input we have second input --------------- #
            final_choice_main_menu = input().lower()
            if final_choice_main_menu == "b":
                # ----- if another choice is the same as first print submenu B choices ----- #
                choice_b()
                # ------------- I used break because continuation wil be in main ------------- #
                break
        elif final_choice_main_menu == "c":
            # --------- this function is a big letters to double-click the letter -------- #
            graphical_ascii_art()
            # --------- display second time a main menu to see a choice for user --------- #
            main_menu_options_display()
            # --------------- again after first input we have second input --------------- #
            final_choice_main_menu = input().lower()
            if final_choice_main_menu == "c":
                # -------------------------- approval of c choice -------------------------- #
                choice_c()
                break
        elif final_choice_main_menu == "x":
            # --------- this function is a big letters to double-click the letter -------- #
            graphical_ascii_art()
            # --------- display second time a main menu to see a choice for user --------- #
            main_menu_options_display()
            # --------------- again after first input we have second input --------------- #
            final_choice_main_menu = input().lower()
            # -------------------- if input is the same break the loop ------------------- #
            if final_choice_main_menu == "x":
                # ------------- I used break because continuation wil be in main ------------- #
                break
        # --------------------------- if input is an error --------------------------- #
        else:
            # ------------------------- print the error message ------------------------- #
            graphical_ascii_wrong_input()
    # ----------------- that return will be used in main function ---------------- #
    return final_choice_main_menu


# ---------------------------------------------------------------------------- #
#                             ----- Section B -----                            #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# -------7. We will now focus on the sub-menu that is displayed should ------- #
# ------------------- the user choose ‘A’ at-the main menu. ------------------- #
# --- The first sub-menu option will allow the user to see all the reviews --- #
# --------------------------- for a specific park. --------------------------- #
# ----- If the user selects this option, then the program should respond ----- #
# ------- by asking which park the user wishes to see the reviews for. ------- #
# -------- The program should then display all reviews for said park. -------- #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# ------------------------------- [A] View data ------------------------------ #
# ------------------------- [A] View Reviews by Park ------------------------- #
# ---------------------------------------------------------------------------- #


# ------------------- that function is park names function ------------------- #
def submenu_a_view_reviews_by_park_initialization():
    # ------- set as unordered dataset will be displaying different park on ------ #
    # ---------------------- every single run o the program ---------------------- #
    # ------------------- used to store park unique park names ------------------- #
    disneyland_parks, file = open_park_data()
    parks_names_unsorted = set()
    # --------------------- loop which is checking the names --------------------- #
    for row in disneyland_parks:
        # ------------------------------ we have 3 parks ----------------------------- #
        if len(parks_names_unsorted) < 3:
            # ------------------------ parks are in 4 index column ----------------------- #
            parks_names_unsorted.add(row[4])
        else:
            break
    # -------- decision to sort the parks and make them static in display -------- #
    parks_names = sorted(parks_names_unsorted)
    file.close()
    # --------------- conversion set to list by personal preferences -------------- #
    return list(parks_names)


# ---------------- function for selected reviews in park names --------------- #4
def submenu_a_view_reviews_by_park_visual_choice(park_names):
    # ----- function to select the park is in the main, but I am changing the ---- #
    # --------- name from park_names to selected_park to not be confusing -------- #
    selected_park = park_names
    # ----------------------------- opening the file ----------------------------- #
    disneyland_parks, file = open_park_data()
    # --------- I am creating empty list to store reviews which will be sorted --- #
    selected_reviews = []
    # --------- displaying the parks with a base of 5 column by the loop --------- #
    for row in disneyland_parks:
        park_name = row[4]
        # ------ if column with index nb 4 is equal to user input add it to list ----- #
        if park_name == selected_park:
            selected_reviews.append(row)
    # ------------------------------ close the file ------------------------------ #
    file.close()
    return selected_reviews


# ----------------------------- sorting the parks ---------------------------- #
# -------------------------------- by reviews -------------------------------- #
def submenu_a_view_reviews_by_park_display_reviews(selected_reviews):
    # ------- sorting by usage of lambda, by second column which (index 1) ------- #
    # --------------------------- in order high to low --------------------------- #
    sorted_reviews = sorted(selected_reviews, key=lambda x: float(x[1]), reverse=True)
    # -------------------------- printing out the parks -------------------------- #
    for review in sorted_reviews:
        # --------------------------- function for printing -------------------------- #
        print_argument(review)


# ---------------------------------------------------------------------------- #
# ------- 8. The second sub-menu option will simply display the number ------- #
# ------ of reviews a specific park has received from a given location. ------ #
# ------- Both the park and the reviewer’s location should be retrieved ------ #
# ------------------------------ from the user. ------------------------------ #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# ------------------------------- [A] View data ------------------------------ #
# ----------- [B] Numbers of Reviews by park and Reviewer Location ----------- #
# ---------------------------------------------------------------------------- #


# ---------------- function for taking localizations from csv ---------------- #
def submenu_a_numbers_of_reviews_by_park_and_reviewer_location_initialization():
    # ----------- I had done it in analogical order to previous task 7. ---------- #
    # ------------------------------- created a set ------------------------------ #
    user_localizations = set()
    # ----------------------------- opening the file ----------------------------- #
    disneyland_parks, file = open_park_data()
    # ----------------------- we have 159 countries in csv ----------------------- #
    for row in disneyland_parks:
        if len(user_localizations) < 159:
            # -------------------- they are in 4 column index number 3 ------------------- #
            user_localizations.add(row[3])
        else:
            break

    # ---- sort in alphabetical order localization to make it easier for user ---- #
    sorted_user_localizations = sorted(list(user_localizations))
    # ------------------------------ close the file ------------------------------ #
    file.close()
    return sorted_user_localizations


# ------------------ function for input, result, and process ----------------- #
def submenu_a_numbers_of_reviews_by_park_and_reviewer_location_visual_choice(
    sorted_user_localizations, selected_park
):
    # ------------- input for location taken for different definition ------------ #
    # ------------------------ function have 2 parameters: ----------------------- #
    # ------------------------- 1. what will be in input ------------------------- #
    # --------------------------------- 2. print --------------------------------- #
    selected_location = choice_input(
        sorted_user_localizations,
        "Choose the reviewer's location: (decimal format): \n",
    )
    # --------------------------- variable for printing -------------------------- #
    x = "\n\t * Reviews for selected park and location: *\n"
    # --------------------------- function for printing -------------------------- #
    # ----- Done it on this way because technically printing is done in TUI, ----- #
    # -------------------- here is just variable with strings -------------------- #
    print_argument(x)
    # ----- calling the function which is counting and doing the list of the ----- #
    # ---- records which are in chosen location and chosen park by the user ---- #
    # ---------------- I am naming this function bt count variable --------------- #
    (
        count
    ) = submenu_a_numbers_of_reviews_by_park_and_reviewer_location_visual_choice_initialization_2(
        selected_park, selected_location
    )
    # --------------------------- variable for printing -------------------------- #
    y = f"\n\tIn reviewer's location: {selected_location}, and park: {selected_park}, there are {count} records.\t\n"
    print_argument(y)
    # --------------------------- function for printing -------------------------- #


# - function for  creating the list with reviews with selected localizations - #
# --------------------- and park names and counting them --------------------- #
def submenu_a_numbers_of_reviews_by_park_and_reviewer_location_visual_choice_initialization_2(
    selected_park, selected_location
):
    # ----------------------------- opening the file ----------------------------- #
    disneyland_parks, file = open_park_data()
    # ----------------- count because I wish to count the review ----------------- #
    count = 0
    # ------------ empty list to append it later with chosen reviews ------------ #
    selected_reviews = []

    # -------- loop which iterates in csv file (checking every single row) ------- #
    for row in disneyland_parks:
        # ----------- variable for park name which is in indexing column 4 ----------- #
        # -------- variable for location (reviewer location) indexing column 3 ------- #
        park_name = row[4]
        location = row[3]

        # --------------- statement if user input is equal to column 4 --------------- #
        # ----------------- and localization is equal to user choice ----------------- #
        if park_name == selected_park and location == selected_location:
            # -------------------------- add record to the list -------------------------- #
            # -------- add count + 1 for every single record which is accepted by -------- #
            # ------------------------------- the statement ------------------------------ #
            selected_reviews.append(row)
            count += 1

    # ----------- calling the function which is sorting the reviews and ---------- #
    # ------------------------------ displaying them ----------------------------- #
    submenu_a_view_reviews_by_park_display_reviews(selected_reviews)
    # ------------------------------ close the file ------------------------------ #
    file.close()

    # -------- returning just count because I wish to have final statement ------- #
    # --------- after displaying the records which is in another function -------- #
    return count


# ---------------------------------------------------------------------------- #
# ---- 9. If the user chooses the third sub-menu option, then the program ---- #
# ------- will ask the user for a park and a year, it will then display ------ #
# ---------- the average rating for the given park in the given year ---------- #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# ------------------------------- [A] View data ------------------------------ #
# -------------------- [C] Average Score per year by Park -------------------- #
# ---------------------------------------------------------------------------- #


# ------- function which is caching up the years and sorting the years ------- #
# -------------------- that will be usefully for user input ------------------- #
def submenu_a_average_score_per_year_by_park_initialization():
    # ------------------- creating the set to avoid duplicates ------------------- #
    years = set()
    # ----------------------------- opening the file ----------------------------- #
    disneyland_parks, file = open_park_data()
    # -- things are getting complicated because year is in the values of YYYY-MM - #
    for row in disneyland_parks:
        # ---- loop which is leading me through 2 indexing column what means years --- #
        year = row[2]
        # --------- I don't want to read the months, so I am using [: number] --------- #
        # ----------------------- which reads first four values ---------------------- #
        year = year[:4]
        # ------------------------- adding the years to a set ------------------------ #
        years.add(year)
    # ----------------------------- closing the file ----------------------------- #
    file.close()

    # ---- sort out the years to always shown up from smallest to highest year --- #
    sorted_years = sorted(years)

    return sorted_years


# ----------------------- fetching the reviews from csv ---------------------- #
def submenu_a_average_score_per_year_by_park_visual_choice(
    sorted_user_year, park_names
):
    # ----- function to select the park is in the main, but I am changing the ---- #
    # --------- name from park_names to selected_park to not be confusing -------- #
    selected_park = park_names

    # -- selected_year calling the function with user choice with 2 parameters: -- #
    # -------- 1. sorted_user_years to display them for user in comfy way -------- #
    # ----------- 2. print for user to make him see what he is choosing ---------- #
    selected_year = choice_input(sorted_user_year, "Select the year: \n")

    # ----------------------------- opening the file ----------------------------- #
    disneyland_parks, file = open_park_data()

    # -------------------------- empty list for reviews -------------------------- #
    selected_reviews = []

    # ------------------ loop which iterates in every row in csv ----------------- #
    for row in disneyland_parks:
        # ------------------- park name is in indexing column nb 4 ------------------- #
        park_name = row[4]
        # ---------------------- year is in indexing column nb 2 --------------------- #
        year = row[2]
        # ----- year is taking 4 first string because the format is looking like: ---- #
        # ---------------------------------- YYYY-MM --------------------------------- #
        year = year[:4]

        # ---- statement which is saying if park name is equal to user choice and ---- #
        # -------------------- year in csv is equal to user choice ------------------- #
        if park_name == selected_park and year == selected_year:
            # -------- if statement is matching adding whole row in the empty list -------- #
            selected_reviews.append(row)
    # ------------------------------ close the file ------------------------------ #
    file.close()
    # ------- calling the function with averages with our selected reviews ------- #
    # ------------------------------- as parameter ------------------------------- #
    submenu_a_average(selected_reviews)


# --------------------------- counting the average --------------------------- #
def submenu_a_average(selected_reviews):
    # ------------------------------ CHALLENGE HERE! ----------------------------- #
    # -- I started to struggling with variables because list is with a strings -- #
    # -------------- and I need to have int, I tried to do it with: -------------- #
    # ---------- https://www.w3schools.com/python/ref_string_isdigit.asp --------- #
    # ---- to understand "insdigit", which is returning true if value is numeric --- #
    # ------------------------------- but I failed ------------------------------- #

    # ---------------------------------------------------------------------------- #
    # ---------------------- So I made a different strategy ---------------------- #
    # ---------------------------------------------------------------------------- #

    # --------- empty list for numeric values because that what I do need -------- #
    numeric_values = []
    # --------------------------- i is just the counter -------------------------- #
    # ------------------ loop is going through selected reviews ------------------ #
    for i in selected_reviews:
        # ----------- if length of the reviews is longer than one  ----------- #
        if len(i) > 1:
            # ------------ adding the things from index 1 to new list like int ----------- #
            numeric_values.append(int(i[1]))

    # ---------------- if there are any records in numeric_values --------------- #
    # -------------------------- that is just validation ------------------------- #
    if numeric_values:
        # ---- because it is list with whole selected_reviews what's mean selected ---- #
        # -------- by user with years I used a sum and / by length of the list ------- #
        # ---------------- I rounded it 2 second place after the coma ---------------- #
        average = round(sum(numeric_values) / len(numeric_values), 2)
        # --------------------------- variable with strings -------------------------- #
        x = f"The average is: {average}"
        # ----------------------------- printing function ---------------------------- #
        print_argument(x)
    # ------------------------ if numeric_values are empty ----------------------- #
    # --------------------------- printing out the dot --------------------------- #
    else:
        y = "."
        print_argument(y)


# ---------------------------------------------------------------------------- #
#                             ----- Section C -----                            #
# ---------------------------------------------------------------------------- #

# -----10. The first sub-menu B option should display a pie chart showing ---- #
# --------------- the number of reviews-each park has received. --------------- #

# ---------------------------------------------------------------------------- #
# ---------------------------- [B] Visualise Data ---------------------------- #
# -------------------------- [A] Most Reviewed Parks ------------------------- #
# ---------------------------------------------------------------------------- #


# ---------- creating the lists which are important to do pie chart ---------- #
def submenu_b_most_reviewed_parks():
    # ---- take the lists from next definitions (lists with reviews for parks) --- #
    (
        paris_reviews,
        hong_kong_reviews,
        california_reviews,
    ) = submenu_b_process_amount_reviews_lists_of_records_each_park()

    # --------------- changing the list and taking the length of it -------------- #
    length_paris_count_reviews = len(paris_reviews)
    length_hong_kong_count_reviews = len(hong_kong_reviews)
    length_california_count_reviews = len(california_reviews)

    # ------------ park names will be useful to subtitles in pie-chart ----------- #
    parks_names = ["Disneyland California", "Disneyland Hong-Kong", "Disneyland Paris"]
    # -------------------------- closing 3 lists in one -------------------------- #
    review_counts = [
        length_paris_count_reviews,
        length_hong_kong_count_reviews,
        length_california_count_reviews,
    ]

    return parks_names, review_counts


# --------- this function is created to save a records from parks in --------- #
# ------------------------------ separated list ------------------------------ #
# ---------- code normalization to not open file every single time ---------- #
def submenu_b_process_amount_reviews_lists_of_records_each_park():
    # ----------------------------- opening the file ----------------------------- #
    disneyland_parks, file = open_park_data()
    # ---------------------- empty list for each of the park --------------------- #
    california_reviews = []
    hong_kong_reviews = []
    paris_reviews = []

    # -------------- loop which iterates in every single row of csv -------------- #
    for row in disneyland_parks:
        # --------------------- park_name is in indexing column 4 -------------------- #
        park_name = row[4]
        # -- if park name is equal to string on right side append the list like int -- #
        if park_name == "Disneyland_California":
            california_reviews.append(int(row[1]))
        elif park_name == "Disneyland_HongKong":
            hong_kong_reviews.append(int(row[1]))
        elif park_name == "Disneyland_Paris":
            paris_reviews.append(int(row[1]))
    # ------------------------------ close the file ------------------------------ #
    file.close()
    # ----------------------------- return the lists ----------------------------- #
    return paris_reviews, hong_kong_reviews, california_reviews


# -------- 11. The second sub-menu option should present the average r ------- #
# -------------- review scores for each park a single bar chart ------------- #

# ---------------------------------------------------------------------------- #
# ---------------------------- [B] Visualise Data ---------------------------- #
# ---------------------------- [B] Average Scores ---------------------------- #
# ---------------------------------------------------------------------------- #


# -------------------- function which counting the average ------------------- #
def submenu_b_average_review_of_each_park():
    # ----------- fetching the park reviews list from previous function ---------- #
    (
        paris_reviews,
        hong_kong_reviews,
        california_reviews,
    ) = submenu_b_process_amount_reviews_lists_of_records_each_park()

    # --------------------- checking the length of the lists --------------------- #
    length_paris_count_reviews = len(paris_reviews)
    length_hong_kong_count_reviews = len(hong_kong_reviews)
    length_california_count_reviews: int = len(california_reviews)

    # ---------- counting the average rounding it to 2 digit after coma ---------- #
    average_paris = round(sum(paris_reviews) / length_paris_count_reviews, 2)
    average_hong_kong = round(
        sum(hong_kong_reviews) / length_hong_kong_count_reviews, 2
    )
    average_california = round(
        sum(california_reviews) / length_california_count_reviews, 2
    )

    # -------- returning the values because that will be utilized in visual ------- #
    return average_california, average_hong_kong, average_paris


# ----- 12. The third sub-menu option will ask the user to enter a park. ----- #
# ------ It will then display a barchart that shows the top 10 locations ----- #


# ---------------------------------------------------------------------------- #
# ---------------------------- [B] Visualise Data ---------------------------- #
# ---------------------- [C] Park Ranking by Nationality --------------------- #
# ---------------------------------------------------------------------------- #
def submenu_b_top_10_countries_averages(park_names):
    # ------- changing the park name to selected park this is the variable ------- #
    # ----------- from park choice input which is processed in main.py ----------- #
    selected_park = park_names
    # ----------------------------- opening the file ----------------------------- #
    disneyland_parks, file = open_park_data()
    # ---------------------- creating the empty directories ---------------------- #
    # -------------- to store the total reviews and count of reviews ------------- #
    reviews = {}
    counts = {}

    # ---------------- loop which iterate through disneyland_parks --------------- #
    for row in disneyland_parks:
        # --------- park name which is in 5 column is equal to park variable --------- #
        park = row[4]
        # ----------------- if park from csv is equal to user choice ----------------- #
        if park == selected_park:
            # -------------- add value from 2 column to reviews like integer ------------- #
            review = int(row[1])
            # ---------------- add value from 4 column without formatting ---------------- #
            country = row[3]
            # ----------------- if park from csv is equal to user choice ----------------- #
            if country not in reviews:
                # ---------- if country is not add country to the both directions --------- #
                reviews[country] = 0
                counts[country] = 0
            # ----------------- add present reviews to the total ratings ----------------- #
            reviews[country] += review
            counts[country] += 1
    # ----------------------------- closing the file ----------------------------- #
    file.close()
    # -- creating new directory with countries which have more than 1 reviews - #
    filtered_averages = {
        country: reviews[country] / counts[country]
        for country in reviews
        if counts[country] > 1
    }
    # ------------------------ sorting in descending order ----------------------- #
    sorted_countries = sorted(
        filtered_averages, key=filtered_averages.get, reverse=True
    )
    # ---------------- return top 10 countries in the sorted list ---------------- #
    # ------------------- and directory with average reviews ------------------ #
    return sorted_countries[:10], {
        country: filtered_averages[country] for country in sorted_countries[:10]
    }


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
def submenu_b_averages_by_the_month_process(park_names):
    # ----------------- import function from tui for park choice ----------------- #
    selected_park = choice_of_the_park_input(park_names)
    # ----------------------------- opening the file ----------------------------- #
    disneyland_parks, file = open_park_data()
    # ---------------- creating a list with numbers of the months ---------------- #
    month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # -------------------------- creating the empty list ------------------------- #
    # -------------------- storage for reviews for each month -------------------- #
    reviews = []
    # -------- loop which is creating the empty list for every single month ------- #
    # ------ I used _ because I didn't want to created variable without use ------ #
    for _ in month_numbers:
        reviews.append([])

    # ----------- loop which is iterated between every single row in csv ---------- #
    for row in disneyland_parks:
        # -------------------------- date is column number 3 ------------------------- #
        date = row[2]
        # ------------------------- date is in format YYYY-MM ------------------------ #
        # -------------- so if we have this "-" symbol in date continue -------------- #
        if "-" in date:
            # ------------ if date has "-", split it between years and months ------------ #
            year, month = date.split("-")
            # ---------------- check if month which is changed to integer ---------------- #
            # -------------------------- is in list month_numbers ------------------------ #
            if int(month) in month_numbers:
                month_index = int(month) - 1
                # ----------------------- add the marks to the reviews ----------------------- #
                reviews[month_index].append(int(row[1]))

    # ------------------------------ close the file ------------------------------ #
    file.close()
    # ---------------------- list to store average variable ---------------------- #
    averages = []

    # -------------------- loop which is going through reviews ------------------- #
    for review in reviews:
        # ------ check if there are any reviews in the month, if there are, calculate average ----- #
        if review:
            average = sum(review) / len(review)
            averages.append(average)
        else:
            averages.append(0)

    return averages, selected_park


# ---------------------------------------------------------------------------- #
#                             ----- Section D -----                            #
# ---------------------------------------------------------------------------- #
# ----- 14. The final sub-menu option for the ‘view data’ menu is to --------- #
# --------- display the average score per park by reviewer location. --------- #
# -------- This, for every park, should output the average rating for -------- #
# ----------------------- every single location it has ----------------------- #
# -------------------------- received a review from. ------------------------- #
# ----- The user should not have to enter any information for this task. ----- #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# ------------------------------- [A] View data ------------------------------ #
# -------------- [D] Average Score per Park by Reviewer Location ------------- #
# ---------------------------------------------------------------------------- #


# ------------------ function which is printing out averages ----------------- #
def submenu_a_averages_by_the_month_process(sorted_user_localizations, park_names):
    # ------------------------------- open the file ------------------------------ #
    disneyland_parks, file = open_park_data()
    # ---------------- I had an idea to store reviews in directory --------------- #
    reviews_by_month = {}

    # --------------------- loop iterating through the program -------------------- #
    for row in disneyland_parks:
        # --------------------------- that is looking like --------------------------- #
        # ------------------------ if park name in park_names ------------------------ #
        # -------------- and reviewer location in sorted user location -------------- #
        if row[4] in park_names and row[3] in sorted_user_localizations:
            # ----------------------- store user location and park ----------------------- #
            tuple_park_name_sorted_user_location = (row[3], row[4])
            # --------- checking if the record is not in directory if not, create -------- #
            # ---------------------------- a new record with 0 --------------------------- #
            if tuple_park_name_sorted_user_location not in reviews_by_month:
                reviews_by_month[tuple_park_name_sorted_user_location] = [0, 0]
            # ------------ append the mark like integer (row nb 1 is the mark) ----------- #
            reviews_by_month[tuple_park_name_sorted_user_location][0] += int(row[1])
            # --------------- increase the count of the reviews in dictionary -------------- #
            reviews_by_month[tuple_park_name_sorted_user_location][1] += 1

    # -------------------------------- close file -------------------------------- #
    file.close()
    # ---------------- loop for counting and printing out averages --------------- #
    for tuple_park_name_sorted_user_location, mark in reviews_by_month.items():
        average = round(mark[0] / mark[1], 2)
        print(
            f"Localization: {tuple_park_name_sorted_user_location[0]}, "
            f"Park: {tuple_park_name_sorted_user_location[1]}, Average: {average}"
        )
