def gen_series(n):
	ai, r = 1, 1
	s = []
	while ai < n:
		s.append(ai)
		r += 1
		ai += r
	return s
	
def md(n):
	return int(n ** 0.5)
	
def main():
	TARGET = 2 * 10 ** 6
	
	s = gen_series(TARGET + TARGET / 5)
	ls = len(s)
	ss = set(s)
	
	d = 1
	while True:
		c = TARGET + d
		mdc = md(c)
		for i in xrange(ls):
			ai = s[i]
			if ai > mdc:
				break
			if c % ai == 0 and c / ai in ss:
				print ai, c / ai, c
				print((i + 1) * (s.index(c / ai) + 1))
				return
		
		d *= -1
		if d > 0:
			d += 1

if __name__ == '__main__':
	main()
