from data import Log
from users import user


def new_log(username):
    with open('log.txt', 'r+') as reader:  # file object for reading and writing
        print("Enter New Journal")
        content = reader.read()     # getting file content into a single object
        journal = input()  # journal string is being entered  by the user
        L = Log(journal)  # making an object of Log class from data.py file
        j = L.get_message()  # getting the journal with timestamp
        reader.seek(0, 0)
        reader.write(username + "$" + j + "\n" + content)  # writing the journal to file
        print("New Log Successfully Written")


def view_log(username):
    try:  # handling the exception if no journal was created yet
        # Hence no file was created successfully
        no_of_journals = 0
        with open('log.txt', 'r') as reader:  # file object for reading
            for i in reader:  # printing the journals
                s_part = list(i.split("$"))
                if s_part[0] == username:
                    print(s_part[1])
                    no_of_journals += 1
                if no_of_journals == 10:
                    break

    except FileNotFoundError or IndexError:
        print("No Journals Yet. Press Y/n to Create New")
        want = input()
        if want == "y" or want == "Y":
            new_log(username)


def main():  # the app runs from here
    username = user()       # making use of users.py file
    stop = "Y"
    while stop != "n":

        print("Enter V to View Logs \nEnter N for Create New Log")
        choice = input()  # getting the user choice to view old or create new journals

        if choice == "N" or choice == "n":
            new_log(username)
        elif choice == "V" or choice == "v":
            view_log(username)

        print("Want to continue (Y/n) ?")  # checking if user wants to continue using the app
        stop = input()


main()  # runner code
