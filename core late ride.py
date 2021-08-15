def lateRide(n):
    a = (n//60)
    b = (n-(60 *a))
    return ((a//10)+(a%10)+(b//10)+(b%10))
