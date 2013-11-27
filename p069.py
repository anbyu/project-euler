def sieve(n):
	candidates = range(n)
	for i in xrange(2, n):
		if candidates[i]:
			candidates[2 * i::i] = [ None ] * ((n - i - 1) / i)
	return [ c for c in candidates[2:] if c ]
	
def program():
	MAX = 10 ** 6
	limit = int(MAX ** 0.5) + 1
	primes = sieve(limit)
	
	n = 1
	for p in primes:
		if n * p > MAX:
			return n
		n *= p

if __name__ == '__main__':
	print program()