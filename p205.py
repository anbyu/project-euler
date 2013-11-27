from __future__ import division

def next(a, mi, ma):
	for i in xrange(1, len(a) + 1):
		if a[-i] < ma:
			a[-i] += 1
			return a
		else:
			a[-i] = mi
	return None

def sums(d, mi, ma):
	a = [ mi ] * d
	yield sum(a)
	a = next(a, mi, ma)
	while a:
		yield sum(a)
		a = next(a, mi, ma)

def main():
	p = sorted(sums(9, 1, 4))
	c = sorted(sums(6, 1, 6))
	
	pi, ci = 0, 0
	lp, lc = len(p), len(c)
	
	d = 0
	
	while ci < lc:
		while pi < lp and p[pi] <= c[ci]:
			pi += 1
		if pi == lp:
			break
		d += lp - pi
		ci += 1
		
	print '{:.7}'.format(d / (lp * lc))
			

if __name__ == '__main__':
	main()