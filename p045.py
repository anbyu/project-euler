def p():
	t, p, h = 285, 165, 143
	t += 1
	tr, pr, hr = 0, 1, 2
	while True:
		while tr < pr:
			tr = t * (t + 1) / 2
			t += 1
		while pr < hr:
			pr = p * (3 * p - 1) / 2
			p += 1
		while hr < tr:
			hr = h * (2 * h - 1)
			h += 1
		if tr == pr and pr == hr:
			return tr

print p()