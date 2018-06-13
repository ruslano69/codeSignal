def firstReverseTry(arr):
    return [arr[len(arr)-x-1] if (x==0)or(x==len(arr)-1) else arr[x] for x in range(0,len(arr))] 