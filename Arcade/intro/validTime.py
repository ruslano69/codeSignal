def validTime(time):
    '''
        return int(time.split(":")[0]) >=0 and int(time.split(":")[0]) <=23 and int(time.split(":")[1]) >=0 and int(time.split(":")[1]) <=60
    '''
    return int(time[0:2]) < 24 and int(time[3:5]) < 60