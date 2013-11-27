def sieve(n):
	primes = range(n)
	limit = int(n ** 0.5 + 1)
	for i in xrange(2, limit):
		if primes[i]:
			primes[i * 2::i] = [ None ] * ((n - 1 - i)/ i)
	return [p for p in primes[2:] if p]

def check_prime(n, primes, lp):
	limit = int(n ** 0.5 + 1)
	for i in xrange(lp):
		p = primes[i]
		if p > limit:
			break
		if n % p == 0:
			return False
	return True
	
def program():
	MAX = 10 ** 5
	primes = sieve(MAX)
	lp = len(primes)
	primes_set = set(primes)
	
	p = 0
	c = 1
	
	n = 1
	a = 2
	s = 1
	r = 1.0
	
	while r > 0.1:
		s += 2
		for i in xrange(4):
			n += a
			if (n < MAX and n in primes_set) or check_prime(n, primes, lp):
				p += 1
			else:
				c += 1
		r = float(p) / (c + p)
		#print p, c+p, s, r
		a += 2
	print s

if __name__ == '__main__':
	program()
