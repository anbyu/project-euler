from common import sieve

def factors(n, primes, sprimes):
	f = []
	for p in primes:
		if n == 1 or p > n:
			break
		while n % p == 0:
			f.append(p)
			n /= p
	return f

def multiply(result, p, pc):
	s, c = 0, 1
	for i in xrange(pc + 1):
		s += c
		c *= p
	return result * s
	
def spd(n, primes, sprimes):
	if n == 1 or n in sprimes:
		return 1
	pds = factors(n, primes, sprimes)
	result = 1
	p, pc = 0, 1
	for d in pds:
		if d != p:
			result = multiply(result, p, pc)
			p, pc = d, 0
		pc += 1
	result = multiply(result, p, pc)
	return result - n

def main():
	MAX = 10 ** 6
	primes = sieve(MAX + 1)
	sprimes = set(primes)
	
	longest = 0
	sums = {}
	for n in xrange(1, MAX + 1):
		s, nums, snums = n, [], set()
		while s <= MAX:
			if s in sums:
				break
			nums.append(s)
			snums.add(s)
			t = spd(s, primes, sprimes)
			sums[s] = t
			s = t
			if s in snums:
				length = len(nums) - nums.index(s)
				if length > longest:
					longest = length
					ans = nums[nums.index(s)]
					print ans
				break
	print ans
	
main()
