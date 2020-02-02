# creating and dealing with users


def check(username):
    with open("user.txt", 'r') as reader:
        for line in reader:
            if username in line:
                return True
    return False


def sign_up():      # signing up
    print("SignUp process\nEnter username:")
    username = input()
    print("Enter password")
    password = input()
    if check(username):
        print("User already exists. Try Again")
        return sign_up()

    with open("user.txt", 'a') as writer:
        writer.write(username + "$" + password+"\n")
        print("User", username, "Signed Up")
    return username


def sign_in():      # signing in already users
    print("Sign In Process\nEnter username:")
    username = input()
    print("Enter password")
    password = input()
    pattern = username + "$" + password
    with open("user.txt", 'r') as reader:
        for line in reader:
            if pattern in line:
                print("Sign In Successful")
                return username
    print("SignIn Unsuccessful")
    return False


def user():
    print("Already a User,SignIn: S\nCreate New User: N")
    choice = input()

    if choice == "N" or choice == "n":
        u = sign_up()
    elif choice == "S" or choice == "s":
        u = sign_in()

    return u


# user()
