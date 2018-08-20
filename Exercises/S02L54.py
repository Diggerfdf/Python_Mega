myfile = open("Files/S02L54.txt", "w")

numbers = [1, 2, 3]

for n in numbers:
    myfile.write(str(n) + "\n")
myfile.close()
