def sum_squares(n):
	m = n
	s = 0
	while m != 0:
		d = m % 10
		s += d * d
		m = m / 10
	return s
	
def calc_chain(n):
	m = n
	while True:
		if m == 1:
			return 1
		if m == 89:
			return 89
		m = sum_squares(m)

def program():
	MAX = 10 ** 7
	limit = sum_squares(MAX - 1)
	
	s1 = set()
	c1, c89 = 0, 0
	for i in xrange(1, limit + 1):
		if calc_chain(i) == 1:
			s1.add(i)
			c1 += 1
		elif calc_chain(i) == 89:
			c89 += 1
	for i in xrange(limit + 1, MAX):
		s = sum_squares(i)
		if s in s1:
			c1 += 1
		else:
			c89 += 1
	print c89

if __name__ == '__main__':
	program()