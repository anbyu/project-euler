def next_m(m):
	return -m if m > 0 else -(m - 1)
	
def sign(m):
	return -1 if m % 2 == 0 else 1

def main():
	MAX = 10 ** 5
	p = [ 1 ]
	for k in xrange(1, MAX + 1):
		m, ki = 1, 1
		pk = 0
		while ki <= k:
			pk += sign(m) * p[k - ki]
			m = next_m(m)
			ki = m * (3 * m - 1) / 2
		if pk % 1000000 == 0:
			print k
			return
		p.append(pk)
	
main()
