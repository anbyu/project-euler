def main():
	TARGET = 10 ** 6
	phis = range(TARGET + 1)
	result = 0
	for i in xrange(2, TARGET + 1):
		p = phis[i]
		if p == i:
			for j in xrange(2 * i, TARGET + 1, i):
				phis[j] = phis[j] / p * (p - 1)
			p -= 1
		result += p
		
	print result

if __name__ == '__main__':
	main()