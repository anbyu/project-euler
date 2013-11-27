def sieve(n):
	candidates = range(n)
	for i in xrange(2, n):
		if candidates[i]:
			candidates[2 * i::i] = [ None ] * ((n - i - 1) / i)
	return [ c for c in candidates[2:] if c ]

def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a
