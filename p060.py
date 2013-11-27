def sieve(n):
	primes = range(n)
	limit = int(n ** 0.5 + 1)
	for i in xrange(2, limit):
		if primes[i]:
			primes[i * 2::i] = [ None ] * ((n - i - 1) / i)
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
	
def check(a, b, primes, primes_set, lp, MAX):
	sa = str(a)
	sb = str(b)
	
	cab = int(sa + sb)
	cba = int(sb + sa)
	
	if cab < MAX:
		if not cab in primes_set:
			return False
	else:
		if not check_prime(cab, primes, lp):
			return False
	if cba < MAX:
		if not cba in primes_set:
			return False
	else:
		if not check_prime(cba, primes, lp):
			return False
	
	return True
	
def program():
	MAX = 10 ** 6
	primes = sieve(MAX)
	primes_set = set(primes)
	lp = len(primes)
	max = len(sieve(10 ** 4))
	
	for i in xrange(max - 4):
		for j in xrange(i + 1, max - 3):
			if not check(primes[i], primes[j], primes, primes_set, lp, MAX):
				continue
			for k in xrange(j + 1, max - 2):
				if not check(primes[i], primes[k], primes, primes_set, lp, MAX):
					continue
				if not check(primes[j], primes[k], primes, primes_set, lp, MAX):
					continue
				for m in xrange(k + 1, max - 1):
					if not check(primes[i], primes[m], primes, primes_set, lp, MAX):
						continue
					if not check(primes[j], primes[m], primes, primes_set, lp, MAX):
						continue
					if not check(primes[k], primes[m], primes, primes_set, lp, MAX):
						continue
					for n in xrange(m + 1, max):
						if not check(primes[i], primes[n], primes, primes_set, lp, MAX):
							continue
						if not check(primes[j], primes[n], primes, primes_set, lp, MAX):
							continue
						if not check(primes[k], primes[n], primes, primes_set, lp, MAX):
							continue
						if not check(primes[m], primes[n], primes, primes_set, lp, MAX):
							continue
						print sum((primes[i], primes[j], primes[k], primes[m], primes[n]))
	
if __name__ == '__main__':
	program()
	