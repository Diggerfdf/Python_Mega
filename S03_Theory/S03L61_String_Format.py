correct_password = "python123"
name = input("Enter name: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password Try Again: ")

print("Hi {0}, you are Logged in.".format(name))

