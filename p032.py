from itertools import combinations, permutations

def to_str(t):
	t = map(str, t)
	return ''.join(t)

def main():
	digits = range(1, 10)
	sdigits = map(str, digits)

	ts = []
	for i in xrange(1, 5):
		ts.extend(combinations(digits, i))
	pts = []
	for t in ts:
		pts.extend(permutations(t))
	strs = map(to_str, pts)
	ints = map(int, strs)
	
	#print ints

	li = len(ints)
	products = set()
	
	for i in xrange(li):
		a = ints[i]
		for j in xrange(i, li):
			b = ints[j]
			c = a * b
			d = ''.join(map(str, (a, b, c)))
			if len(d) != 9:
				continue
			ok = True
			for digit in sdigits:
				if not digit in d:
					ok = False
					break
			if ok:
				print a, b, c
				products.add(c)
				
	return sum(products)
	
print main()