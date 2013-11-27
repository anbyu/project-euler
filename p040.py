def p():
	c = 1
	i = 1
	le = 0
	
	digits = []
	
	while c <= 10 ** 6:
		si = str(i)
		lsi = len(si)
		le += lsi
		if le >= c:
			digits.append(si[c-le+lsi-1])
			c *= 10
		i += 1
	digits = map(int, digits)
	
	print digits
	
	r = 1
	for d in digits:
		r *= d
	
	return r
	
print p()