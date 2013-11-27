def sieve(n):
	primes = range(n + 1)
	primes[0:2] = [None] * 2
	lp = len(primes)
	
	for i in xrange(lp):
		p = primes[i]
		if p:
			primes[i * 2::i] = [None] * ((n - i) / i)
	
	return primes
	
def p(limit):
	primes = sieve(limit)
	lp = len(primes)
	total = 0
	
	for i in xrange(11, lp):
		p = primes[i]
		if p:
			s = str(p)
			ls = len(s)
			ok = True
			for i in xrange(1, ls):
				tl = int(s[i:ls])
				if not primes[tl]:
					ok = False
					break
				tr = int(s[0:ls - i])
				if not primes[tr]:
					ok = False
					break
			if ok:
				total += p
				print p
	return total
	
print p(10 ** 6)