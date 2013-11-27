def main(n):
	maxcount = 0
	maxp = 0
	for p in xrange(1, n + 1):
		count = 0
		print '', p
		for a in xrange(1, (p + 1) / 3):
			if (p * p - 2 * p * a) % (2 * p - 2 * a) == 0:
				b = (p * p - 2 * p * a) / (2 * p - 2 * a)
				c = p - a - b
				print a, b, c
				count += 1
		if count > maxcount:
			maxcount = count
			maxp = p
	return maxp
			
print main(1000)