def main():
	LIMIT = 10 ** 6
	
	a, b = 3, 7
	r, s = 0, 1
	
	for q in xrange(LIMIT, 2, -1):
		p = (a * q - 1) / b
		if r * q < p * s:
			r, s = p, q
	print '{}/{}'.format(r, s)

if __name__ == '__main__':
	main()