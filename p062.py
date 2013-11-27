from time import clock
from itertools import permutations

def program():
	r = 0
	i = 0
	cubes = {}
	while r != 4:
		n = i * i * i
		h = ''.join(sorted(list(str(n))))
		s, r = cubes.get(h, [None, 0])
		cubes[h] = [n if not s else s, r + 1]
		i += 1
	print s
	
if __name__ == '__main__':
	start = clock()
	program()
	print clock() - start, 's'