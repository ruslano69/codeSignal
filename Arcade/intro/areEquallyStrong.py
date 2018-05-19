def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    yourWeakest = yourLeft if yourLeft <= yourRight else yourRight
    yourStrongest = yourLeft if yourLeft > yourRight else yourRight
    friendWeakest = friendsLeft if friendsLeft <= friendsRight else friendsRight
    friendStrongest = friendsLeft if friendsLeft > friendsRight else friendsRight
    
    return yourWeakest == friendWeakest and yourStrongest == friendStrongest