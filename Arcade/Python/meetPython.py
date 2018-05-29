# For evaluating Python Category problems
'''
Collections Truthness: [True, False]

Efficient Comparison: Option 1 is the most optimal one

Special Conditional: a == not b

Language Differences: x = 15, y = -4


'''

def countBits(n):
    return n.bit_length()

	
def modulus(n):
    if type(n) == int :
        return n % 2
    else:
        return -1
		
def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr

def baseConversion(n, x):
    return '{0:x}'.format(int(n,x))

def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found
	
def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        _,*res,_ = res
    return res
