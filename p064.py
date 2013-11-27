def main():
	MAX = 10000
	ans = 0
	for n in xrange(2, MAX + 1):
		a0 = int(n ** 0.5)
		if a0 * a0 == n:
			continue
		an, mn, dn = a0, 0, 1
		tri = [ (mn, dn, an) ]
		while True:
			mn1 = dn * an - mn
			dn1 = (n - mn1 * mn1) / dn
			an1 = (a0 + mn1) / dn1
			t = (mn, dn, an) = (mn1, dn1, an1)
			try:
				period = len(tri) - tri.index(t)
				if period % 2 == 1:
					ans += 1
				break
			except:
				tri.append(t)
	print(ans)

if __name__ == '__main__':
	main()