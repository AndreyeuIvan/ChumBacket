def to_jaden_case(string):
    #return string.title()
    return " ".join([x.capitalize() for x in string.split(" ")])


print(to_jaden_case('How can mirrors be real if our eyes arent real'))

