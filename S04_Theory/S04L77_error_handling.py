def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You are dividing by Zero"


print(divide(1, 0))
print("End of program")
