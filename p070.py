from __future__ import division
from common import sieve

def is_perm(a, b):
	sa, sb = str(a), str(b)
	return len(sa) == len(sb) and sorted(sa) == sorted(sb)

def main():
	MAX = 10 ** 7
	lb = int(MAX ** 0.5) - 1000
	ub = int(MAX ** 0.5) + 1000
	
	primes = [ p for p in sieve(ub) if p > lb ]
	
	min_ratio = MAX
	dat_n = None
	for i in xrange(len(primes)):
		for j in xrange(i + 1, len(primes)):
			p1, p2 = primes[i], primes[j]
			n = p1 * p2
			if n > MAX:
				break
			phi = (p1 - 1) * (p2 - 1)
			ratio = n / phi
			if ratio < min_ratio and is_perm(n, phi):
				min_ratio = ratio
				dat_n = n
				
	print dat_n
	
if __name__ == '__main__':
	main()