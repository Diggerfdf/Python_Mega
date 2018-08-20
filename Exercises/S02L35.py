def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers doesn´t have length"
    elif type(mystring) == float:
        return "Sorry, floats doesn´t have length"
    else:
        return len(mystring)


print(string_length("hello"))
print(string_length(10))
print(string_length(10.65))
