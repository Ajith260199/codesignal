def isIPv4Address(inputString):
    count = 0
    a = list(inputString.split('.'))
    try:
        if len(a)==4:
            for i in a:
                if i != "":
                    count +=1
                    if count == 4:
                            for i in a:
                                if int(i) <= 255 and i!="00" and i!="01":
                                    print(i)
                                else:
                                    return False                 
                else:
                    return False
            return True                                
    except ValueError:
        return False           
    else:
        return False

   
