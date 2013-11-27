def sieve(n):
	candidates = range(n)
	for i in xrange(2, n):
		if candidates[i]:
			candidates[2 * i::i] = [ None ] * ((n - i - 1) / i)
	return [ c for c in candidates[2:] if c ]

def lower_bound(p, a):
	lenp = len(p)
	l, r = 0, lenp
	while l < r and l != r - 1:
		t = (r - l) / 2 + l
		if p[t] > a:
			r = t
		else:
			l = t
	return p[r:]

def has_family(s, d, sprimes):
	f = 0
	for c in '0123456789':
		n = int(s.replace(d, c))
		if n in sprimes:
			f += 1
	return f == 8
	
def main():
	MIN = 10 ** 5
	MAX = 10 ** 6
	primes = sieve(MAX)
	primes = lower_bound(primes, MIN)
	sprimes = set(primes)
	
	for p in primes:
		s = str(p)
		if s.count('0') == 3 and has_family(s, '0', sprimes) \
		or s.count('1') == 3 and s[-1] != '1' and has_family(s, '1', sprimes) \
		or s.count('2') == 3 and has_family(s, '2', sprimes):
			print(s)
			break
	
if __name__ == '__main__':
	main()