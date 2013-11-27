def sieve(n):
	primes = range(n + 1)
	primes[0:2] = [None] * 2
	lp = len(primes)
	for i in xrange(2, lp):
		p = primes[i]
		if p:
			primes[2 * i::i] = [None] * ((n - i) / i)
	return [p for p in primes if p]
	
def main(n):
	primes = sieve(n)
	primes_set = set(primes)
	
	primes_sums = [0]
	c = 0
	s = 0
	while s < n:
		s += primes[c]
		primes_sums.append(s)
		c += 1
		
	t = 1
	maxp = 0
	for i in xrange(c):
		for j in xrange(i + t, c):
			n = primes_sums[j] - primes_sums[i]
			if j - i > t and n in primes_set:
				t, maxp = j - i, n
				
	return (t, maxp)

print main(10 ** 6)