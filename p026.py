def p(limit):
	maxcount = 0
	for d in xrange(2, limit + 1):
		c = 1
		cs = set([])
		counting = False
		count = 0
		while c % d != 0:
			c = (c % d) * 10
			if counting:
				count += 1
				if c == start:
					break
			if c in cs and not counting:
				counting = True
				start = c
			cs.add(c)
		if count > maxcount:
			maxcount = count
			maxd = d
	return maxd
	
print p(1000)