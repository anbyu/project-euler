from __future__ import division

def hcb(a, b):
	while b != 0:
		a, b = b, a % b
	return a

def main():
	MAX = 12000
	a, b = 1, 3
	c, d = 1, 2
	
	ans = 0
	
	for p in xrange(1, MAX):
		lb = 2 * p + 1
		ub = 3 * p
		if lb > MAX:
			continue
		if ub > MAX + 1:
			ub = MAX + 1
		for q in xrange(lb, ub):
			if hcb(q, p) == 1:
				ans += 1
	print(ans)
	

if __name__ == '__main__':
	main()