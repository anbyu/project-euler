def c(n, r):
	p = 1
	for s in xrange(r + 1, n + 1):
		p *= s
	
	for s in xrange(2, n - r + 1):
		p /= s
	return p

def main():
	total = 0
	for n in xrange(1, 101):
		for r in xrange(1, n + 1):
			cc = c(n, r)
			if cc > 1000000:
				print n, r, cc
				total += 1
	return total

print main()
#print c(23, 10)