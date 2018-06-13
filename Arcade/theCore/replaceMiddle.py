def replaceMiddle(arr):
    if len(arr) % 2 == 0:
        ans = []
        for i in range(len(arr)):
            if i == len(arr)//2-1:
                ans.append(arr[len(arr)//2-1]+arr[len(arr)//2])
            elif i == len(arr)//2:
                continue
            else:
                ans.append(arr[i])
        return ans
    else:
        return arr
