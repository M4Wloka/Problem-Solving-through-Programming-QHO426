# ----------------- json and csv are necessary to do 15 task ----------------- #
import json
import csv

# ------------ global variable, because we will need it all the time ----------- #
file_path_main = "data/disneyland_reviews.csv"


# ------ because that is name of the class I used different naming system ----- #
# --------------------- https://peps.python.org/pep-0008/ -------------------- #
class DisneylandReviewsReader:
    def __init__(self, file_path):
        self.file_path_main = file_path

    # -------- function which is opening the csv and converting it to csv -------- #
    def lists_with_reviews(self):
        # ----------------------------- opening the file ----------------------------- #
        with open(self.file_path_main, newline="") as csvfile:
            disneyland_parks = csv.reader(csvfile)
            # --------------------------- we don't want header --------------------------- #
            next(disneyland_parks)
            # ------------------ creating 3 lists for separated reviews ------------------ #
            paris, hong_kong, california = [], [], []
            # -------- loop which is adding reviews to each lists by the park name ------- #
            for row in disneyland_parks:
                if "Disneyland_Paris" == row[4]:
                    # --------------- adding the reviews like int instead of string -------------- #
                    paris.append(int(row[1]))
                elif "Disneyland_HongKong" == row[4]:
                    # --------------- adding the reviews like int instead of string -------------- #
                    hong_kong.append(int(row[1]))
                elif "Disneyland_California" == row[4]:
                    # --------------- adding the reviews like int instead of string -------------- #
                    california.append(int(row[1]))

        return california, hong_kong, paris


class DisneylandDataProcessor:
    def __init__(self, reviews_reader):
        self.reviews_reader = reviews_reader
        self.data = self.process_data()

    # ------------ definition which is converting directory to csv ------------ #
    # --------------------- idea of this definition is from: --------------------- #
    # ------- https://kl1p.com/python-dictionary-to-csv-with-code-examples/ ------ #
    # ----------------------------- x is directory ---------------------------- #
    @staticmethod
    def dict_to_csv(x):
        # -------------------------- creating 2 empty lists -------------------------- #
        field, entry = [], []
        # -------------- k- which is key is looping though directory -------------- #
        for k in x:
            field.append(k)
            entry.append(x[k])
            # ---------- adding items to the lists to make it look like 2 lists ---------- #
            # ---------------------------- instead directory --------------------------- #
        return field, entry

    # ---------------------- function with number of reviews --------------------- #
    def nb_of_reviews(self):
        # ---------- taking the lists from the class DisneylandReviewsReader ---------- #
        california, hong_kong, paris = self.reviews_reader.lists_with_reviews()
        # --------------------- counting the length of the lists --------------------- #
        california_length = len(california)
        hong_kong_length = len(hong_kong)
        paris_length = len(paris)

        return california_length, hong_kong_length, paris_length

    # ----------------------- function for positive reviews ---------------------- #
    def positive_reviews(self):
        # ---------- taking the lists from the class DisneylandReviewsReader ---------- #
        california, hong_kong, paris = self.reviews_reader.lists_with_reviews()
        # ----------------- creating empty lists with positive reviews ---------------- #
        positive_california = []
        positive_hong_kong = []
        positive_paris = []
        # ----------------- I made decision after talk with lecturer ----------------- #
        # ------------------- that positive review is greater than 3 ------------------ #
        # ----- so I created the loops which are adding positive review to lists ----- #
        for row in california:
            if row > 3:
                positive_california.append(row)
        for row in hong_kong:
            if row > 3:
                positive_hong_kong.append(row)
        for row in paris:
            if row > 3:
                positive_paris.append(row)

        return positive_california, positive_hong_kong, positive_paris

    # ---------- function which counts how many countries made the review --------- #
    def lists_of_countries(self):
        # ------------------ I made decision to open the file again ------------------ #
        # ----- because before I added to the lists just reviews not a countries ----- #
        with open(self.reviews_reader.file_path_main, newline="") as csvfile:
            disneyland_parks = csv.reader(csvfile)
            # -------------------------------- skip header ------------------------------- #
            next(disneyland_parks)
            # --------- creating the sets because I want to store unique elements -------- #
            # --------------------------- and avoid duplicates -------------------------- #
            paris_countries, hong_kong_countries, california_countries = (
                set(),
                set(),
                set(),
            )
            # ------------------- loop which is iterating in csv file ------------------- #
            for row in disneyland_parks:
                if row[4] == "Disneyland_Paris":
                    # ---------------------- adding the country to the set ---------------------- #
                    paris_countries.add(row[3])
                elif row[4] == "Disneyland_HongKong":
                    # ---------------------- adding the country to the set ---------------------- #
                    hong_kong_countries.add(row[3])
                elif row[4] == "Disneyland_California":
                    # ---------------------- adding the country to the set ---------------------- #
                    california_countries.add(row[3])

        # ------------------- returning the length because I don't ------------------- #
        # ------------------ want to read the names of the countries ----------------- #
        # --------------------------- just number how many --------------------------- #
        return len(paris_countries), len(hong_kong_countries), len(california_countries)

    # ------------------- counting the averages of the reviews ------------------- #
    def average_reviews(self):
        # ------------- taking the lists with reviews from first class ------------ #
        california, hong_kong, paris = self.reviews_reader.lists_with_reviews()

        # -------------------------- calculating the ravage -------------------------- #
        california_average = sum(california) / len(california)
        hong_kong_average = sum(hong_kong) / len(hong_kong)
        paris_average = sum(paris) / len(paris)

        return california_average, hong_kong_average, paris_average

    # ------- definition which is processing outcomes of the function above ------- #
    def process_data(self):
        # --------------------- taking the numbers of the reviews -------------------- #
        california_length, hong_kong_length, paris_length = self.nb_of_reviews()
        # -------------------------- taking positive reviews ------------------------- #
        (
            positive_california,
            positive_hong_kong,
            positive_paris,
        ) = self.positive_reviews()
        # ---------------------------- taking the averages --------------------------- #
        california_average, hong_kong_average, paris_average = self.average_reviews()
        # ----------------------- taking list of the countries ----------------------- #
        (
            paris_countries,
            hong_kong_countries,
            california_countries,
        ) = self.lists_of_countries()

        # ---- returning full directory with filled data from the functions above ---- #
        # ---------------------- this is my personal experiment ---------------------- #
        return {
            "Disneyland_Paris": {
                "Location": "Paris",
                "Number of reviews": paris_length,
                "Number of positive reviews": len(positive_paris),
                "Average review score": paris_average,
                "Number of countries that have reviewed": paris_countries,
            },
            "Disneyland_California": {
                "Location": "California",
                "Number of reviews": california_length,
                "Number of positive reviews": len(positive_california),
                "Average review score": california_average,
                "Number of countries that have reviewed": california_countries,
            },
            "Disneyland_HongKong": {
                "Location": "Hong-Kong",
                "Number of reviews": hong_kong_length,
                "Number of positive reviews": len(positive_hong_kong),
                "Average review score": hong_kong_average,
                "Number of countries that have reviewed": hong_kong_countries,
            },
        }

    # --------------------------- exporting of the data -------------------------- #
    # ---------------------- I had done it like on website: ---------------------- #
    # -------------------- https://realpython.com/python-json/ ------------------- #
    # ------- fileoutput is the string which provide the final file export ------- #
    def export(self, fileoutput):
        # ------------------------ if user choice will be json ----------------------- #
        if fileoutput == "json":
            # ----------------------- opening file in writing mode ----------------------- #
            with open("parks_data.json", "w") as outfile:
                # -------- json.dump() - function used to write data in the json file -------- #
                # --------------- outfile the object where will be data written -------------- #
                # -------------------------- indentation is 4 spaces ------------------------- #
                json.dump(self.data, outfile, indent=4)
        # ----------------------- when user choice will be csv ----------------------- #
        elif fileoutput == "csv":
            # --------------------------- open in writing mode --------------------------- #
            with open("parks_data.csv", "w") as outfile:
                # -------------------------- creating writer object -------------------------- #
                write = csv.writer(outfile)
                # ---- for each park it calls the dict_to_csv function with a park variables --- #
                for park in self.data:
                    # --------------------- calling the dict_to_csv function --------------------- #
                    # ---------------------------- f= field, e=entries --------------------------- #
                    f, e = self.dict_to_csv(self.data[park])
                    # ------------------------------ writing one row ----------------------------- #
                    write.writerow(f)
                    # ---------------------------- writing another row --------------------------- #
                    write.writerow(e)
        # ----------------------- if user will choose txt file ----------------------- #
        elif fileoutput == "txt":
            with open("parks_data.txt", "w") as outfile:
                outfile.write(str(self.data))


class DisneylandDataPrint:
    def __init__(self, reviews_reader):
        self.reviews_reader = reviews_reader
        self.data = DisneylandDataProcessor(reviews_reader).process_data()

    # ----------------------- function for reading the data ---------------------- #
    def print_data(self):
        # ------------------ loop which is going through self.data ------------------ #
        for park_name, data in self.data.items():
            print(park_name)
            # ------------ putting the variables from directory to print below ----------- #
            for left_headers, counted_data in data.items():
                print(f"{left_headers}: {counted_data}")
            # -------------------------------- formatting -------------------------------- #
            print()


# ------------------- initialization of saving file in json ------------------ #
def save_data_to_json():
    # ----------------- creating the object read a file from CSV ----------------- #
    reviews_reader = DisneylandReviewsReader(file_path_main)

    # ---------------------- processing the data - counting ---------------------- #
    data_processor = DisneylandDataProcessor(reviews_reader)

    # ----------------------------- exporting to json ---------------------------- #
    data_processor.export("json")

    # --------- calling the data which will be displaying on the console -------- #
    disneyland_data = DisneylandDataPrint(reviews_reader)
    disneyland_data.print_data()


# ------------------- initialization of saving file in csv ------------------- #
def save_data_to_csv():
    # ----------------- creating the object read a file from CSV ----------------- #
    reviews_reader = DisneylandReviewsReader(file_path_main)

    # ---------------------- processing the data - counting ---------------------- #
    data_processor = DisneylandDataProcessor(reviews_reader)

    # ----------------------------- exporting to csv ----------------------------- #
    data_processor.export("csv")

    # --------- calling the data which will be displaying on the console -------- #
    disneyland_data = DisneylandDataPrint(reviews_reader)
    disneyland_data.print_data()


# ------------------- initialization of saving file in txt ------------------- #
def save_data_to_txt():
    # ----------------- creating the object read a file from CSV ----------------- #
    reviews_reader = DisneylandReviewsReader(file_path_main)

    # ---------------------- processing the data - counting ---------------------- #
    data_processor = DisneylandDataProcessor(reviews_reader)

    # ----------------------------- exporting to txt ----------------------------- #
    data_processor.export("txt")

    # --------- calling the data which will be displaying on the console -------- #
    disneyland_data = DisneylandDataPrint(reviews_reader)
    disneyland_data.print_data()
