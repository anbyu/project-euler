from itertools import permutations

def tuple2num(t):
	m = 1
	s = 0
	for n in t[::-1]:
		s += n * m
		m *= 10
	return s

def main():
	primes = [ 2, 3, 5, 7, 11, 13, 17 ]
	lp = len(primes)
	digits = range(10)

	total = 0
	
	perms = permutations(digits)
	for t in perms:
		ok = True
		for i in xrange(lp):
			n = t[i + 1] * 100 + t[i + 2] * 10 + t[i + 3]
			if n % primes[i] != 0:
				ok = False
				break
		if ok:
			total += tuple2num(t)
	return total
	
print main()