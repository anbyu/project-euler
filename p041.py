def sieve(n):
	primes = range(n + 1)
	primes[0:2] = [None] * 2
	for i in xrange(2, n):
		p = primes[i]
		if p:
			primes[i * 2::i] = [None] * ((n - i) / i)
	return [i for i in primes if i]
	
def main(n):
	print "Generating up to", n, "digit primes...",
	primes = sieve(10 ** n)
	print "OK"
	
	primes = map(str, primes)
	digits = map(str, range(1, n + 1))
	
	for p in primes:
		ok = True
		for d in digits:
			if not d in p:
				ok = False
		if ok:
			print p
			
print main(7)
	