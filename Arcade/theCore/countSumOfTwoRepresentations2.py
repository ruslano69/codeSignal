def countSumOfTwoRepresentations2(n, l, r):
	counter = 0
	
	for i in range(l,r+1):
		if (n-i) >= l and (n-i) <= r and (n-i) >= i:
			counter += 1
	return counter