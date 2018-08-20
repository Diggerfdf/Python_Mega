import glob2
from datetime import datetime

filenames = glob2.glob("/home/digger/Classes/Python_Mega/Exercises/Files/S03L72/*.txt")

with open("/home/digger/Classes/Python_Mega/Exercises/Files/S03L72/" + datetime.now()
        .strftime("%Y-%m%d-%H-%M-%S-%f") + ".txt", "w") as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read() + "\n")
