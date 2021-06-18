def chessBoardCellColor(cell1, cell2):
        c = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        a = list(cell1)
        b = list(cell2)
        if a[0] and b[0] in c:
            if c.index(a[0])%2==0 and c.index(b[0])%2==0 and int(a[1])%2!=0 and int(b[1])%2==0:
                return False 
            if c.index(a[0])%2==0 and c.index(b[0])%2!=0 and int(a[1])%2!=0 and int(b[1])%2==0:
                return True
            if c.index(a[0])%2==0 and c.index(b[0])%2!=0 and int(a[1])%2!=0 and int(b[1])%2!=0:
                return False 
            if c.index(a[0])%2==0 and c.index(b[0])%2==0 and int(a[1])%2!=0 and int(b[1])%2!=0:
                return True
            if c.index(a[0])%2!=0 and c.index(b[0])%2!=0 and int(a[1])%2!=0 and int(b[1])%2!=0:
                return True
            if c.index(a[0])%2==0 and c.index(b[0])%2==0 and int(a[1])%2!=0 and int(b[1])%2==0:
                return True
            if c.index(a[0])%2!=0 and c.index(b[0])%2!=0 and int(a[1])%2==0 and int(b[1])%2==0:
                return True
            if c.index(a[0])%2==0 and c.index(b[0])%2!=0 and int(a[1])%2==0 and int(b[1])%2==0:
                return False 
            if c.index(a[0])%2!=0 and c.index(b[0])%2!=0 and int(a[1])%2!=0 and int(b[1])%2==0:
                return False 
            if c.index(a[0])%2!=0 and c.index(b[0])%2==0 and int(a[1])%2!=0 and int(b[1])%2!=0:
                return False 
            if c.index(a[0])%2!=0 and c.index(b[0])%2!=0 and int(a[1])%2==0 and int(b[1])%2!=0:
                return False
            if c.index(a[0])%2==0 and c.index(b[0])%2!=0 and int(a[1])%2==0 and int(b[1])%2==0:
                return False  
            if c.index(a[0])%2==0 and c.index(b[0])%2==0 and int(a[1])%2==0 and int(b[1])%2!=0:
                return False
            if c.index(a[0])%2!=0 and c.index(b[0])%2==0 and int(a[1])%2!=0 and int(b[1])%2==0:
                return False        
