def sieve(n):
	a = range(n + 1)
	a[0:2] = [ None, None ]
	for i in xrange(n):
		if a[i]:
			a[i * 2::i] = [ None ] * ((n - i) / i)
	primes = []
	composites = []
	for i in xrange(2, n):
		if a[i]:
			primes.append(i)
		elif i % 2 != 0:
			composites.append(i)
	return (primes, composites)

def main():
	(primes, composites) = sieve(10 ** 6)
	for c in composites:
		found = False
		for p in primes:
			if not found:
				if p > c:
					return c
				i = 1
				val = p
				while val < c:
					val = p + 2 * i * i
					if val == c:
						found = True
						break
					i += 1
			else:
				break
print main()