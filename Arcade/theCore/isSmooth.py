def isSmooth(arr):
    if len(arr)%2==0:
        return arr[0]==arr[len(arr)-1] and arr[0]== (arr[len(arr)//2-1]+arr[len(arr)//2])
    else:
        return arr[0]==arr[len(arr)-1] and arr[0]== arr[(len(arr)-1)//2];