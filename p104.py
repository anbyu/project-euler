from math import log10

def is_pandigital(n):
	sn = str(n)
	if len(sn) != 9:
		return
	ssn = set(sn)
	return len(ssn) == 9 and not '0' in ssn
	
def main():
	logfi = log10((1 + 5 ** 0.5) / 2)
	logsq5 = log10(5 ** 0.5)
	a, b = 1, 1
	i = 2
	tail = 10 ** 9
	found = False
	while not found:
		c = (a + b) % tail
		a, b = b, c
		i += 1
		if is_pandigital(c):
			p = i * logfi - logsq5
			front = int(10 ** (p - int(p) + 8))
			if is_pandigital(front):
				found = True
	print i
	
main()