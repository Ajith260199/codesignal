
def arrayMaximalAdjacentDifference(inputArray):
    temp1=[] 
    for i in range(len(inputArray)-1):
        temp = inputArray[i]-inputArray[i+1]
        temp1.append(abs(temp))
    return max(temp1)
