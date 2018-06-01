def rounders(value):
    carry = counter = 0
    ans = ""
    
    for num in str(value)[::-1]:
        if counter == len(str(value)) - 1:
			val = int(num) + carry
			if val == 10:
				ans += "0"
			ans += str(val)
			return int(ans[::-1])
		if int(num) + carry < 5:
			ans += "0"
			carry = 0
		else:
			ans += "0"
			carry = 0
		counter += 1