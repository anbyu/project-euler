def permutations(n):
	perms = [ 1 ]
	if n == 0:
		return perms
	c = 1
	for i in xrange(1, n + 1):
		c *= i
		perms.append(c)
	return perms

def p(n, limit):
	b = limit + 1
	m = n - 1
	digits = range(b);
	perms = permutations(b)
	lp = len(perms)
	result = []
	for i in xrange(b, 0, -1):
		p = perms[i]
		r = perms[i - 1]
		d = digits[m / r];
		digits.remove(d)
		result.append(str(d))
		m %= r
	return ''.join(result)
	
print p(10**6, 9)