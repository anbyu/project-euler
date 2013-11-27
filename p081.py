def read_matrix():
	file = 'matrix.txt'
	#file = 'matrix_small.txt'
	matrix = []
	with open(file) as f:
		for line in f:
			matrix.append(map(int, line.split(',')))
	return matrix

def update(matrix, i, j):
	if i == 0:
		if j > 0:
			matrix[i][j] += matrix[i][j - 1]
	else:
		if j == 0:
			matrix[i][j] += matrix[i - 1][j]
		else:
			matrix[i][j] = min(matrix[i][j] + matrix[i][j - 1], matrix[i][j] + matrix[i - 1][j])
			
def program():
	matrix = read_matrix()
	nrows, ncols = len(matrix), len(matrix[0])
	for i in xrange(nrows):
		for j in xrange(ncols):
			update(matrix, i, j)
	print matrix[nrows - 1][ncols - 1]

if __name__ == '__main__':
	program()