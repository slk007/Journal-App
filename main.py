import data

choice = input("enter s to view log or e to enter new log")

if choice is "e":
    file = open("log.txt", "r+")
    t = input("enter the text")
    file.write(t.log.get_message())
    file.close()
else:
    file = open("log.txt", "r+")
    file.read(5)
    file.close()
