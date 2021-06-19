def arrayReplace(inputArray, elemToReplace, substitutionElem):
    if elemToReplace in inputArray:
        for i in range(len(inputArray)):
            if elemToReplace == inputArray[i]:
                inputArray[i]=substitutionElem
        return inputArray
                
    else:
        return inputArray
