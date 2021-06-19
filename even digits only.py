def evenDigitsOnly(n):
    a = (list(str(n)))
    for i in a:
        if int(i)%2!=0:
            return False
    return True
   
    
            
        
