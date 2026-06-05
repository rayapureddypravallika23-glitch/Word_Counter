file_name = input("Enter file name: ")

try:
    with open(file_name, "r") as file:
        content = file.read()

    words = content.split()

    print("Total number of words:", len(words))

except FileNotFoundError:
    print("File not found!") 