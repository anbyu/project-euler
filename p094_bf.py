def area(a, b):
	b2 = b / 2.0
	h = (a * a - b2 * b2) ** 0.5
	return b * h

def main():
	MAX = 10 ** 9
	limit = MAX / 3 + 1
	s = 0
	for a in xrange(2, limit):
		if a % 10 ** 7 == 0:
			print a
		ar = area(a, a + 1)
		if ar == int(ar):
			s += 3 * a + 1
		ar = area(a, a - 1)
		if ar == int(ar):
			s += 3 * a - 1
	print s
main()
