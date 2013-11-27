def ds(n):
	s = 0
	while n != 0:
		s += n % 10
		n /= 10
	return s

def main():
	maxds = 0
	for a in xrange(100):
		for b in xrange(100):
			s = ds(a ** b)
			if s > maxds:
				print a, b, s
				maxds = s 
	return maxds

print main()