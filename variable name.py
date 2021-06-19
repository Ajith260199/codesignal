def variableName(name):
    charValues = [48,  49,  50,  51,  52,  53,  54,  55,  56,  57, 95, 97,  98,  99,  100, 101, 102, 103, 104, 105,      106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    listName = [i for i in str(name)]
    if listName[0] in str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        return False
    for i in range(len(listName)):
        if ord(listName[i].lower()) not in charValues:
            return False
    return True
