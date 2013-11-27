def sieve(n):
    limit = int(n ** 0.5)
    candidates = range(n + 1)
    
    for i in xrange(2, limit + 1):
        if not candidates[i]:
            continue
            
        candidates[2 * i::i] = [None] * (n / i - 1)
        
    return [i for i in candidates[2:] if i]

def p():
	maxa = 1000
	maxb = 1000
	limit = 1000000
	print "Generating primes... ", 
	primes = set(sieve(limit))
	print "OK."
	maxc = 0
	for a in xrange(-maxa, maxa + 1):
		for b in xrange(-maxb, maxb + 1):
			n = 0
			c = 0
			while True:
				r = n * n + a * n + b
				if r in primes:
					c += 1
					n += 1
				else:
					break
			if c > maxc:
				maxc = c
				result = a * b
				print a, b, maxc
	return result

print p()