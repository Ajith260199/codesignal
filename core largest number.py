# def largestNumber(n):
#     a = []
#     while len(a)<n:
#         a.append(9)
#         strings = [str(a) for a in a]
#         a_string = "".join(strings)
#         an_integer = int(a_string)
#     return an_integer

def largestNumber(n):
    return int(n*"9")
