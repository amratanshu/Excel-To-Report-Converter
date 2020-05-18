def isSrNo(string):
    splitString = string.split(".")
    if string == '':
        return False
    if splitString[0].islower():
        return False
    if len(splitString[0]) != 1:
        return False
    for i in range(1, len(splitString)):
        if not splitString[i].isdigit():
            return False
    return True

def getNestingLevel(sr_no):
    return sr_no.count('.')