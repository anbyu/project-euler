def main():
	MAX = 10 ** 6
	a = 2
	count = 0
	while count <= MAX:
		a += 1
		aa = a * a
		for bc in xrange(3, 2 * a + 1):
			s = (aa + bc * bc) ** 0.5
			if s == int(s):
				count += bc / 2 if bc <= a else 1 + (a - (bc + 1)/ 2)
	print a, count
	
main()
