from common import gcd

def main():
	MAX = 50
	ans = MAX * MAX * 3
	for x in xrange(1, MAX + 1):
		for y in xrange(1, MAX + 1):
			g = gcd(x, y)
			ans += 2 * min((MAX - x) * g / y, y * g / x)
	print ans

main()