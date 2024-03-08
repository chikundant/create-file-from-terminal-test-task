from datetime import datetime
from sys import argv
from os import mkdir, chdir

filename = ""
directories = []

# Use function with descriptive name to cover up some logic
# Remember about KISS and DRY code principle
# Variable should be specified inside function or classes to prevent any conflicts.
# Global vars we can use for values that are not supposed to be changed during the run

if "-f" in argv:
    # Instead of if/else, if you have multiple flags/options
    # better to user dicts and enums like:
    # flags: dict = {"-f": some_function}
    index = 0

    for _ in range(len(argv) - 1):
        # The _ sign can be used only if we need to receive some value, but we are not going to use it
        index += 1
        if argv[_: _ + 1] == ["-f"]:
            break

    filename = argv[index]

    if "-d" in argv:
        index2 = 0

        for _ in range(len(argv) - 1):
            index2 += 1
            if argv[_: _ + 1] == ["-d"]:
                break

        directories = argv[index2:index - 1]
else:
    filename = "file.txt"

    if "-d" in argv:
        index = 0

        for _ in range(len(argv) - 1):
            index += 1
            if argv[_: _ + 1] == ["-d"]:
                break

        directories = argv[index:len(argv)]

file_data = [datetime.today().strftime('%y:%d:%m %H-%M-%S'), "\n"]

while True:
    line = input("Enter content line: ")
    if line == "exit":
        break
    file_data.extend([line])

for directory in directories:
    try:
        mkdir(directory)
    except Exception:
        # Better to user your own Exception class with descriptive name instead of regular exception
        # MyException(Exception): pass
        pass
    chdir(directory)

with open(filename, "w") as f:
    f.writelines(file_data)
