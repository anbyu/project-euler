def sieve(n):
	candidates = range(n)
	for i in range(2, n):
		if candidates[i]:
			candidates[2 * i::i] = [ None ] * ((n - i - 1) / i)
	return [ c for c in candidates[2:] if c ]

def find_div(n, primes):
	limit = int(n ** 0.5) + 1
	for p in primes:
		if p > limit:
			return None
		if n % p == 0:
			return p
	
	
def program():
	MAX = 10
	limit = int(MAX ** 0.5) + 1
	primes = sieve(limit)
	lp = len(primes)
	phi = [ 0 ] * (MAX + 1)
	
	curr = 2
	for i in xrange(1, lp):
		prev, curr = curr, primes[i]
		phi[prev] = prev - 1
		for n in xrange(prev + 1, curr):
			d = find_div(n, primes)
			e = n / d
			if d != e:
				phi[n] = phi[d] * phi[n / d]
			else:
				phi[n] = n - 1 - (n - 1) / d
	
	n = curr
	while n <= MAX:
		d = find_div(n, primes)
		if d:
			e = n / d
			if d != e:
				phi[n] = phi[d] * phi[n / d]
			else:
				phi[n] = n - 1 - (n - 1) / d
		else:
			phi[n] = n - 1
		n += 1
	
	max = 0.0
	for n in range(2, MAX + 1):
		p = phi[n]
		r = float(n) / p
		print n, p, r
		if r > max:
			max = r
			max_n = n
	print max_n
		
if __name__ == '__main__':
	program()