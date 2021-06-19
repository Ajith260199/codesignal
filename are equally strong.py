def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):

        if yourLeft==friendsLeft and yourRight==friendsRight:
            return True
        elif yourRight==friendsLeft and yourLeft==friendsRight:
            return True
        else:
            return False
