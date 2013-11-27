from itertools import combinations

def sieve(m, n):
	primes = range(n + 1)
	primes[0:2] = [ None ] * 2
	for i in xrange(2, n):
		if primes[i]:
			primes[i * 2::i] = [ None ] * ((n - i) / i)
	return [ p for p in primes if p and p > 1000 ]

def are_perms(t):
	(a, b, c) = map(set, map(list, map(str, t)))
	if a == b and b == c:
		return True
	else:
		return False
	
	
def main():
	primes = sieve(1000, 10000)
	
	combs = combinations(primes, 3)
	
	answers = []
	
	for t in combs:
		if t[2] - t[1] == t[1] - t[0]:
			if are_perms(t):
				answers.append(''.join(map(str, t)))
	return answers
	
print main()