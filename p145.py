def main():
	LIMIT = 10

	s = 0

	for n in xrange(1, 10):
		print n - 1, s
		if n % 4 == 1: continue
		elif n % 2 == 0: s += 20 * 30 ** (n / 2 - 1)
		else: s += 5 * 20 ** ((n - 3) / 4 + 1) * 25 ** ((n - 3) / 4)
		
	print s

if __name__ == '__main__':
	main()