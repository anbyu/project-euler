def sieve(n):
	candidates = range(n)
	for i in xrange(2, n):
		if candidates[i]:
			candidates[2 * i::i] = [ None ] * ((n - i - 1)/ i)
	return [c for c in candidates[2:] if c]

def phi(n, primes, primes_set):
	if n in primes_set:
		return n - 1
	limit = n / 2 + 1
	divisors = []
	lp = len(primes)
	tn = n
	for i in xrange(lp):
		p = primes[i]
		if p > limit:
			break
		s = 0
		while tn % p == 0:
			s += 1
			tn /= p
		if s != 0:
			divisors.append((p, s))
	result = 1
	for p, k in divisors:
		result *= p ** (k - 1) * (p - 1)
	return result

def program():
	MAX = 10
	primes = sieve(MAX)
	primes_set = set(primes)
	#ratio = 4.0/10.0
	ratio = 15499.0/94744.0
	r = 1
	d = 1
	while r >= ratio:
		d += 1
		p = phi((d), primes, primes_set)
		r = p / float(d - 1)
		if d % 10 ** 4 == 0:
			print d, p, r
	print d

def test():
	primes = sieve(1000)
	primes_set = set(primes)
	for i in xrange(1, 11):
		print i, phi(i, primes, primes_set)
		
if __name__ == '__main__':
	program()
	#test()