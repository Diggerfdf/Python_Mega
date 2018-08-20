my_file = open("Files/fruits_2.txt")
content = my_file.read()
my_file.close()
content = content.splitlines()

for i in content:
    print(len(i))
