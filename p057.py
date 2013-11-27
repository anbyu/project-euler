def next(a, i):
	return 2 * a[i - 1] + a[i - 2]

def program():
	MAX = 1000
	n = [0] * (MAX + 1)
	d = [0] * (MAX + 1)
	
	n[:2] = 1, 3
	d[:2] = 1, 2
	
	count = 0
	
	for i in xrange(2, MAX + 1):
		n[i] = next(n, i)
		d[i] = next(d, i)
		if len(str(n[i])) > len(str(d[i])):
			count += 1
	return count

if __name__ == '__main__':
	print program()