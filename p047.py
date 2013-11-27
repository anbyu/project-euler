def sieve(n):
	primes = range(n + 1)
	primes[0:2] = [ None ] * 2
	for i in xrange(2, n):
		if primes[i]:
			primes[i * 2::i] = [ None ] * ((n - i) / i)
	return [ p for p in primes if p ]

def get_distinct_prime_factors(n, primes):
	limit = int(n / 2)
	factors = set()
	for p in primes:
		if p > limit:
			break
		if n % p == 0:
			factors.add(p)
	return factors
	
def is_ok(n, fn, primes):
	factors = get_distinct_prime_factors(n, primes)
	return len(factors) == fn
	
def main(fn):
	print 'sieve...',
	primes = sieve(10 ** 7)
	print 'ok'
	i = 2
	c = 0
	while True:
		if is_ok(i, fn, primes):
			c += 1
			if c == fn:
				return i - fn + 1
		else:
			c = 0
		
		i += 1
	
print main(4)