def program():
	a, b = 2, 3
	m = 1
	
	for n in xrange(3, 101):
		if n % 3 == 0:
			a, b = b, a + b + b * m
			m += 2
		else:
			a, b = b, a + b
	print sum(map(int, list(str(b))))
	
if __name__ == '__main__':
	program()