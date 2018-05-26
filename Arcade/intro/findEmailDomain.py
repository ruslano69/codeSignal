def findEmailDomain(address):
    local = address
    while local[-1]!='@':
        local = address[0:len(local)-1]
    
    return address[len(local):]
