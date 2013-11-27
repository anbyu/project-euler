from common import sieve

def main():
	MAX = 100
	primes = sieve(MAX)
	ways = [ 1 ] + [ 0 ] * MAX
	for p in primes:
		for i in xrange(p, MAX + 1):
			ways[i] += ways[i - p]
	for i in xrange(len(ways)):
		if ways[i] > 5000:
			print i
			return

main()