def read_matrix():
	file = 'matrix.txt'
	#file = 'matrix_small.txt'
	matrix = []
	with open(file) as f:
		for line in f:
			matrix.append(map(int, line.split(',')))
	return matrix

def main():
	matrix = read_matrix()
	n = len(matrix)
	
	for j in xrange(n - 1):
		candidates = [ [] for i in xrange(n) ]
		for i in xrange(n):
			a = matrix[i][j]
			candidates[i].append(a + matrix[i][j + 1])
			for ii in xrange(i - 1, -1, -1):
				candidates[ii].append(candidates[ii + 1][i] + matrix[ii][j + 1])
			for ii in xrange(i + 1, n):
				candidates[ii].append(candidates[ii - 1][i] + matrix[ii][j + 1])
		for i in xrange(n):
			matrix[i][j + 1] = min(candidates[i])
	print min([ matrix[i][n - 1] for i in xrange(n) ])
		
if __name__ == '__main__':
	main()