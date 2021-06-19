def reverseInParentheses(inputString):
    char = list(inputString)
    open_bracket = []
    for i,c in enumerate(char):
        if c=='(':
            open_bracket.append(i)
        elif c==')':
            j = open_bracket.pop()
            char[j:i]= char[i:j:-1]
    return ''.join(c for c in char if c not in '()')
