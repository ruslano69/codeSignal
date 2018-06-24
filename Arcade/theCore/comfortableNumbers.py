def comfortableNumbers(l, r):
	if l == r:
		return 0
		
	a = l
	b = a + 1
	sumA = 0
	pairs = 0
	
	while a < r:
		a_str = str(a)
		a_X = 0
		
		while a_X < len(a_str):
			sumA += int(a_str[a_X])
			a_X += 1
		while b <= r:
			b_str = str(b)
			b_X = 0
			sumB = 0
			while b_X < len(b_str):
				sumB += int(b_str[b_X])
				b_X += 1
			if (b >= a - sumA) and (b <= a + sumA) and (a >= b - sumB) and (a <= b + sumB):
				pairs += 1
			b += 1
		a += 1
		b = a + 1
		sumA = 0
	return pairs
			