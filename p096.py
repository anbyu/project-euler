from copy import deepcopy

def print_sudoku(sudoku):
	print '-----------------'
	for i in xrange(9):
		for j in xrange(9):
			if len(sudoku[i][j]) == 1:
				print list(sudoku[i][j])[0],
			elif len(sudoku[i][j]) == 0:
				print 0,
			else:
				print 'X',
		print
	print '-----------------'

def read_sudokus():
	filename = 'sudoku.txt'
	#filename = 'sudoku_small.txt'
	with open(filename) as f:
		while len(f.readline().rstrip()) > 0:
			sudoku = [ None for i in xrange(9) ]
			for i in xrange(9):
				line = f.readline().rstrip()
				numbers = map(int, list(line))
				sudoku[i] = map(set, [ [ n ] if n != 0 else [] for n in numbers ])
			yield sudoku

def get_related(i, j):
	related = set([])
	for ii in xrange(9):
		if ii != i:
			related.add((ii, j))
	for jj in xrange(9):
		if jj != j:
			related.add((i, jj))
	bi, bj = i / 3 * 3, j / 3 * 3
	for ii in xrange(3):
		for jj in xrange(3):
			ci = bi + ii
			cj = bj + jj
			if ci != i and cj != j:
				related.add((ci, cj))
	return related
	
def get_candidates(i, j, sudoku, related, digits):
	s = set()
	for ii, jj in related[i][j]:
		t = sudoku[ii][jj]
		if len(t) == 1:
			s.update(t)
	candidates = digits.difference(s)
	return candidates

def is_solved(sudoku):
	for i in xrange(9):
		for j in xrange(9):
			if len(sudoku[i][j]) != 1:
				return False
	return True

def is_erroneous(sudoku):
	is_0 = False
	is_uncertain = False
	for i in xrange(9):
		for j in xrange(9):
			if len(sudoku[i][j]) == 0:
				is_0 = True
			if len(sudoku[i][j]) > 1:
				is_uncertain = True
	erroneous = is_0 and not is_uncertain
	return erroneous
	
	
def update_definite(sudoku, related, digits):
	changed = True
	while changed:
		changed = False
		for i in xrange(9):
			for j in xrange(9):
				s = sudoku[i][j]
				if len(s) == 0 or len(s) > 1:
					sudoku[i][j] = get_candidates(i, j, sudoku, related, digits)
				if len(s) != len(sudoku[i][j]):
					changed = True

def get_smallest_set(sudoku):
	min_ls = 10
	for i in xrange(9):
		for j in xrange(9):
			ls = len(sudoku[i][j])
			if ls > 1 and ls < min_ls:
				min_ls = ls
				mi, mj = i, j
	return (mi, mj, min_ls)
	
def solve(sudoku, related, digits):
	stack = [ sudoku ]
	while len(stack) > 0:
		sudoku = stack.pop()
		update_definite(sudoku, related, digits)
		if is_erroneous(sudoku):
			continue
		if is_solved(sudoku):
			return sudoku
			
		si, sj, ls = get_smallest_set(sudoku)
		#print si, sj, ls
		for i in xrange(ls):
			s = deepcopy(sudoku)
			s[si][sj] = set([sudoku[si][sj].pop()])
			stack.append(s)
	return None
	
def main():
	related = [ [ get_related(i, j) for j in xrange(9) ] for i in xrange(9)]
	digits = set(range(1, 10))

	s = 0
	i = 0
	for sudoku in read_sudokus():
		solved = solve(sudoku, related, digits)
		i += 1
		print i
		print_sudoku(solved)
		s += 100 * solved[0][0].pop() + 10 * solved[0][1].pop() + solved[0][2].pop()
	print s
	
main()
