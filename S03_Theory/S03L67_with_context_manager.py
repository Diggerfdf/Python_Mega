myfile = open("example.txt", "w")
myfile.write("Something")
myfile.close()

with open("example.txt", "w") as myfile:
    myfile.write("Something else")

# The above statement is preferable. "With open" takes care of the Close argument
