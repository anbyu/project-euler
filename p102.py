def cp(a, b, c):
	ab = (b[0] - a[0], b[1] - a[1])
	ac = (c[0] - a[0], c[1] - a[1])
	return ab[0] * ac[1] - ab[1] * ac[0]

def contains_mid(triangle):
	a, b, c = triangle[0:2], triangle[2:4], triangle[4:6]
	z = (0, 0)
	
	cpabz, cpbcz, cpcaz = cp(a, b, z), cp(b, c, z), cp(c, a, z)
	
	return (cpabz >= 0 and cpbcz >= 0 and cpcaz >= 0) \
		or (cpabz <= 0 and cpbcz <= 0 and cpcaz <= 0)

def main():
	s = 0
	with open('triangles.txt') as f:
		for line in f:
			triangle = map(int, line.rstrip().split(','))
			if contains_mid(triangle):
				s += 1
	print(s)

if __name__ == '__main__':
	main()
