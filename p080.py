def digital_sum(n, limit):
	c, p = n, 0
	sum = 0
	for i in xrange(limit):
		x = 0
		while x * (20 * p + x) <= c:
			x += 1
		x -= 1
		y = x * (20 * p + x)
		p = 10 * p + x
		sum += x
		c -= y
		if c == 0:
			return 0
		else:
			c *= 100
	return sum

def main():
	ans = 0
	for i in xrange(2, 100):
		ans += digital_sum(i, 100)
	print ans

if __name__ == "__main__":
	main()