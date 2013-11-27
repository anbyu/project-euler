from collections import deque


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
	li, lj = len(matrix), len(matrix[0])
	total = sum([ sum(matrix[i]) for i in xrange(li) ])
	sums = [ [ total + 1 for j in xrange(li) ] for i in xrange(li) ]
	sums[0][0] = matrix[0][0]
	d = deque([ (0, 0) ])
	while len(d) > 0:
		i, j = d.pop()
		if i > 0 and sums[i][j] + matrix[i - 1][j] < sums[i - 1][j]:
			sums[i - 1][j] = sums[i][j] + matrix[i - 1][j]
			d.appendleft((i - 1, j))
		if i < li - 1 and sums[i][j] + matrix[i + 1][j] < sums[i + 1][j]:
			sums[i + 1][j] = sums[i][j] + matrix[i + 1][j]
			d.appendleft((i + 1, j))
		if j > 0 and sums[i][j] + matrix[i][j - 1] < sums[i][j - 1]:
			sums[i][j - 1] = sums[i][j] + matrix[i][j - 1]
			d.appendleft((i, j - 1))
		if j < lj - 1 and sums[i][j] + matrix[i][j + 1] < sums[i][j + 1]:
			sums[i][j + 1] = sums[i][j] + matrix[i][j + 1]
			d.appendleft((i, j + 1))
	print sums[li - 1][lj - 1]

	
main()
