def equal(li1, li2):
	le = len(li1)
	for i in xrange(le):
		if li1[i] != li2[i]:
			return False
	return True

def p():
	x = 1
	n = x * 10
	skip = False
	
	while True:
		ok = True
		sx = str(x)
		lx = sorted(list(sx))
		
		for i in xrange(6, 1, -1):
			xx = x * i
			sxx = str(xx)
			if len(sxx) != len(sx):
				x = n - 1
				n *= 10
				ok = False
				break
			lxx = sorted(list(sxx))
			if not equal(lx, lxx):
				ok = False
				break
		
		if ok:
			for i in range(2, 7):
				print x * i,
			print
			return x
		
		x += 1

print p()