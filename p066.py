def solved(A, B, n):
	return A[-1] * A[-1] - n * B[-1] * B[-1] == 1

def main():
	MAX = 1000
	ans = 0
	for n in xrange(2, MAX + 1):
		a0 = int(n ** 0.5)
		if a0 * a0 == n:
			continue
		an, mn, dn = a0, 0, 1
		A = [ a0 ]
		B = [ 1 ]
		while not solved(A, B, n):
			mn1 = dn * an - mn
			dn1 = (n - mn1 * mn1) / dn
			an1 = (a0 + mn1) / dn1
			
			if len(A) == 1:
				A.append(an1 * a0 + 1)
				B.append(an1)
			else:
				A.append(an1 * A[-1] + A[-2])
				B.append(an1 * B[-1] + B[-2])
			
			(mn, dn, an) = (mn1, dn1, an1)
		if A[-1] > ans:
			ans = A[-1]
			print n, ans
	print(ans)
	
if __name__ == '__main__':
	main()

	