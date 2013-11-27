def pd(n):
	if n == 0 or n == 1:
		return []
	d = [ 1 ]
	append = d.append
	limit = int(n ** 0.5)
	for li in xrange(2, limit + 1):
		if n % li == 0:
			append(li)
			s = n / li
			if s != li:
				append(s)
	return d
	
def fa(b):
	an = []
	app = an.append
	for i in xrange(2, b + 1):
		d = pd(i)
		if sum(d) > i:
			app(i)
	return an

def fs(n):
	an = fa(n)
	s = set([])
	add = s.add
	for i in an:
		for j in an:
			if i + j <= n:
				add(i + j)
	nrs = sorted(list(s))
	ni = 0
	total = 0
	for i in xrange(1, n + 1):
		if i < nrs[ni]:
			total += i
		while i >= nrs[ni]:
			ni += 1
			if ni >= len(nrs):
				break
	return total
		
	
print fs(28123)