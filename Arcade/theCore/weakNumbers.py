def weakNumbers(n):
	rainbow = {1:1}
	for i in range(2, n+1):
		weaknesses = 1
		for num in range(1, i):
			if (float(i) / float(num)).is_integer():
				rainbow[i] = weaknesses
	weakest = 0
	sameVal = 0
	newRainbow = {}
	for i in range(1, n + 1):
		weakness = 0
		for j in range(1, i):
			if rainbow[i] < rainbow[j]:
				weakness += 1
		if weakness > weakest:
			weakest = weakness
		newRainbow[i] = weakness
		
	for k, v in newRainbow.items():
		if weakest == v:
			sameVal += 1
	return [weakest, sameVal]