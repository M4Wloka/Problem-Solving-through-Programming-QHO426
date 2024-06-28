"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


# ---------------------------------------------------------------------------- #
#                             ----- Section A -----                            #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# -------------------- 1. First, when running the program, ------------------- #
# --------------------- it should display the following: --------------------- #
# ---------------------------------------------------------------------------- #


def welcome():
    invitation = "Disneyland Review Analyser"
    separator = "-"

    # ----------------------------- (len(invitation)) ---------------------------- #
    # --------------------- checking the length of the string -------------------- #
    # ----------------- printing the welcome message with 26 "-" ---------------- #
    print(f"\n{(len(invitation)) * separator}")
    print(invitation)
    print(f"{(len(invitation)) * separator} \n")


# ---------------------------------------------------------------------------- #
# -------------- 2. Read in the data from the provided CSV file, ------------- # +
# ------------- said data should be stored in a list. The program ------------ #
# -------------- should confirm to the user when it has finished ------------- #
# -------------------------- reading in the dataset. ------------------------- #
# -------------- It should also tell the user how many rows are -------------- #
# ------------------------------ in the dataset. ----------------------------- #
# ---------------------------------------------------------------------------- #


# --- wor number will be counted in process that's why I prefer to call the -- #
# ---------------------- function in process than in tui --------------------- #
def row_number_display(rows_nb):
    print(f"Number of rows in Disneyland Reviews is: \n\t * {rows_nb} *\n")


# ---------------------------------------------------------------------------- #
# ------ 3. Output the following to the screen, this will act as a menu.  ----- #
# ---- The user should then be able to input their selection, which should --- #
# --------------------- be stored in a suitable variable. -------------------- #
# ---------------------------------------------------------------------------- #
def main_menu_options_display():
    print(
        "\n\nPlease enter the letter which corresponds with your desired menu choice: \n \t[A] View data \n\t"
        "[B] Visualise Data \n\t[C] Export the data\n\t[X] Exit"
    )


def main_menu_input():
    menu_choice = str(input().lower())
    # ---------------- providing lowercase input to avoid user mistakes ---------------- #
    # ---------------------- menu choice is stored in string --------------------- #
    # ---------------------------------------------------------------------------- #
    return menu_choice


# ---------------------------------------------------------------------------- #
# ----------4. The program should confirm what the user has entered. --------- #
# --------------- If the user enter invalid menu choice,  ---------------- #
# -------------- then they should be informed of their mistake. -------------- #
# ---------------------------------------------------------------------------- #


def menu_choice_confirmation(menu_choice):
    if menu_choice == "a":
        print("You have chosen option A - View Data")
    elif menu_choice == "b":
        print("You have chosen option B - Visualise Data")
    elif menu_choice == "c":
        print("You have chosen option C - Export the data")
    elif menu_choice == "x":
        print("You have chosen option X - Exit")
    else:
        print("Wrong input, please try again")


# ---------------------------------------------------------------------------- #
# ------------- 6. If the user selects ‘A’ as their menu choice, ------------- #
# ----------------- the program should display the following ----------------- #
# --------------------------------- sub-menu --------------------------------- #
# ---------------------------------------------------------------------------- #


def choice_a():
    print("Please enter one of the following option:")
    print("\t[A] View Reviews by Park")
    print("\t[B] Numbers of Reviews by park and Reviewer Location")
    print("\t[C] Average Score per year by Park")
    print("\t[D] Average Score per Park by Reviewer Location\n")


def submenu_choice():
    # ----------------- Section B provide development of the code ---------------- #
    submenu_user_choice = str(input().lower())
    # -------------------- submenu choice is stored in string -------------------- #
    # ---------------------------------------------------------------------------- #
    return submenu_user_choice


# ----------------------------- submenu A choices ---------------------------- #
def submenu_a_choice_confirmation(submenu_user_choice):
    if submenu_user_choice == "a":
        print("You have chosen option A - View Reviews by Park")
    elif submenu_user_choice == "b":
        print(
            "You have chosen option B - Numbers of Reviews by park and Reviewer Location"
        )
    elif submenu_user_choice == "c":
        print("You have chosen option C - Average Score per year by Park")
    elif submenu_user_choice == "d":
        print("You have chosen option D - Average Score per Park by Reviewer Location")
    else:
        print("Wrong input, please try again")


# ---------------------------------------------------------------------------- #
# --------------6. If the user selects ‘B’ as their menu choice, ------------- #
# ------------- the program should display the following sub-menu ------------ #
# ---------------------------------------------------------------------------- #


# ----------------------------- submenu B choices ---------------------------- #
def choice_b():
    print("Please enter one of the following option:")
    print("\t[A] Most Reviewed Parks")
    print("\t[B] Average Scores")
    print("\t[C] Park Ranking by Nationality")
    print("\t[D] Most Popular per Month by Park\n")


# ------ graphical ascii make user aware for double-clicking the letter ------ #
# ---- that is my personal preference because after checking and checking ---- #
# -------------------- I stopped to see this notification -------------------- #
def graphical_ascii_art():
    ascii_approve_message_1 = """


┏┓┓                ┓    
┃┃┃┏┓┏┓┏┏┓  ┏┓┏┓┏┏┓┃┏┓┏╋
┣┛┗┗ ┗┻┛┗   ┛ ┗ ┛┗ ┗┗ ┗┗
                        


 ┓     ┓        
╋┣┓┏┓  ┃┏┓╋╋┏┓┏┓
┗┛┗┗   ┗┗ ┗┗┗ ┛ 
                

                                                                                                                                                    
    """
    ascii_approve_message_2 = """
 
                      ┓      ┓   •   
╋┏┓  ┏┓┏┓┏┓┏┓┏┓┓┏┏┓  ╋┣┓┏┓  ┏┣┓┏┓┓┏┏┓
┗┗┛  ┗┻┣┛┣┛┛ ┗┛┗┛┗   ┗┛┗┗   ┗┛┗┗┛┗┗┗ 
       ┛ ┛                           
                                     
    """
    return print(ascii_approve_message_1), print(ascii_approve_message_2)


# --- graphical ASCII is always nice to see by user to avoid input mistakes -- #
# ---- that is my personal preference because after checking and checking ---- #
# -------------------- I stopped to see this notification -------------------- #
def graphical_ascii_wrong_input():
    ascii_wrong_message_1 = """
┓ ┏          •       
┃┃┃┏┓┏┓┏┓┏┓  ┓┏┓┏┓┓┏╋
┗┻┛┛ ┗┛┛┗┗┫  ┗┛┗┣┛┗┻┗
          ┛     ┛          
    """
    ascii_wrong_message_2 = """
┏┳┓            •  
 ┃ ┏┓┓┏  ┏┓┏┓┏┓┓┏┓
 ┻ ┛ ┗┫  ┗┻┗┫┗┻┗┛┗
      ┛     ┛     
    """
    return print(ascii_wrong_message_1), print(ascii_wrong_message_2)


def print_reviews_for_selected_park():
    print("Reviews for selected park:")


# ---------------------------------------------------------------------------- #
#                             ----- Section C -----                            #
# ---------------------------------------------------------------------------- #
# --------- to start section C I started to organize the B - submenu -------- #
def submenu_b_choice_confirmation(submenu_user_choice):
    if submenu_user_choice == "a":
        print("You have chosen option A - Most Reviewed Parks")
    elif submenu_user_choice == "b":
        print("You have chosen option B - Average Scores")
    elif submenu_user_choice == "c":
        print("You have chosen option C - Park Ranking by Nationality")
    elif submenu_user_choice == "d":
        print("You have chosen option D - Most Popular per Month by Park\n")
    else:
        graphical_ascii_wrong_input()


def submenu_c_choice_confirmation(submenu_user_choice):
    if submenu_user_choice == "a":
        print("You have chosen option A - JSON")
    elif submenu_user_choice == "b":
        print("You have chosen option B - CSV")
    elif submenu_user_choice == "c":
        print("You have chosen option C - TXT")
    else:
        graphical_ascii_wrong_input()


def print_argument(x):
    print(x)


# ------------------- choice of year and localizations etc. ------------------ #
def choice_input(choices, prompt_message):
    while True:
        print(prompt_message)
        for i, choice in enumerate(choices):
            print(f"\t{i + 1}. * {choice} *\n")

        random_choice_input = input(
            "Enter the number of your choice or type 'exit' to come back to the main menu:\n"
        )
        if random_choice_input.lower() == "exit":
            return None

        try:
            choice_index = int(random_choice_input) - 1  # Fix here
            if 0 <= choice_index < len(choices):
                selected_choice = choices[choice_index]
                print(f"You selected: {selected_choice}")
                return selected_choice
            else:
                graphical_ascii_wrong_input()
        except ValueError:
            graphical_ascii_wrong_input()


# ----------------------------- park choice input ---------------------------- #
def choice_of_the_park_input(park_names):
    while True:
        print("Which park do you want to choose? (1, 2, 3)\n")
        for i, park_name in enumerate(park_names):
            print(f"\t{i + 1}. * {park_name} *\n")

        choice_park = input(
            "Enter the number of your choice or type 'exit' to come back to main menu:\n"
        )
        if choice_park.lower() == "exit":
            return None

        try:
            choice_of_the_park = int(choice_park) - 1
            if 0 <= choice_of_the_park < 3:
                selected_park = park_names[choice_of_the_park]
                # -------------------------- confirmation of choice -------------------------- #
                print(f"You selected: {selected_park}")
                return selected_park
            else:
                graphical_ascii_wrong_input()
        except ValueError:
            graphical_ascii_wrong_input()


def choice_c():
    print("Please enter one of the following option:")
    print("\t[A] JSON")
    print("\t[B] CSV")
    print("\t[C] TXT")
