def get_pns(n):
	pns = []
	for i in xrange(1, n + 1):
		pns.append(i*(3*i-1)/2)
	return pns

def f():
	n = 10 ** 4
	pns = get_pns(n)
	spns = set(pns)
	
	results = []
	
	for i in xrange(n):
		a = pns[i]
		for j in xrange(i, n):
			b = pns[j]
			if a + b in spns and b - a in spns:
				results.append(b - a)
	
	print min(results)
	
f()