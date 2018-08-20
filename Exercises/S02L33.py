def string_length(mystring):
    if type(mystring) == int:
        return "Sorry integers doesn't have length"
    else:
        return len(mystring)

string_length(10)
