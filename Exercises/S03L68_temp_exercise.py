temperatures = [10, -20, -289, 100]


def writer(temperatures):
    with open("Files/temps.txt", "w") as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9/5 + 32
                file.write(str(f) + "\n")


writer(temperatures)

# Second and better solution, to treat both the temperature input and the file path
# as function arguments:

"""
temperatures = [10, -20, -289, 100]


def writer(temperatures, filepath):
    with open(filepath, "w") as file: 
        for c in temperatures:
            if c > -273.15:
                f = c * 9/5 + 32
                file.write(str(f) + "\n"
                

writer(temperatures, "Files/temps.txt"
"""