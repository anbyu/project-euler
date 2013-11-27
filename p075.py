def check(tuple, max):
	return tuple[0] > tuple[1] and 2 * tuple[0] * (tuple[0] + tuple[1]) <= max

def get_coprimes(max):
	stack = [ (2, 1) ]
	coprimes = []
	while len(stack) > 0:
		cp = stack.pop()
		a = (2 * cp[0] - cp[1], cp[0])
		b = (2 * cp[0] + cp[1], cp[0])
		c = (2 * cp[1] + cp[0], cp[1])
		if check(a, max):
			stack.append(a)
		if check(b, max):
			stack.append(b)
		if check(c, max):
			stack.append(c)
		coprimes.append(cp)
	return coprimes

def main():
	TARGET = 1500000
	coprimes = get_coprimes(TARGET)
	Ls = [ 0 ] * (TARGET + 1)
	for m, n in coprimes:
		L = 2 * m * (m + n)
		k = 1
		while k * L < TARGET + 1:
			Ls[k * L] += 1
			k += 1
	s = sum(map(lambda x: 1 if x == 1 else 0, Ls))
	print(s)
	
main()
