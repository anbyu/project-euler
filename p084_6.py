from random import randint, shuffle

def next_r(i):
	if i >= 35 or i < 5:
		return 5
	elif i < 15:
		return 15
	elif i < 25:
		return 25
	elif i < 35:
		return 35

def next_u(i):
	if i >= 28 or i < 12:
		return 12
	elif i < 28:
		return 28
		
def get_new_cc_pos(c, pos):
	if c == 1:
		pos = 0
	elif c == 2:
		pos = 10
	return pos

def get_new_ch_pos(c, pos):
	if c == 1:
		pos = 0
	elif c == 2:
		pos = 10
	elif c == 3:
		pos = 11
	elif c == 4:
		pos = 24
	elif c == 5:
		pos = 39
	elif c == 6:
		pos = 5
	elif c == 7 or c == 8:
		pos = next_r(pos)
	elif c == 9:
		pos = next_u(pos)
	elif c == 10:
		pos -= 3
	return pos

def roll(pos):
	SIDES = 6
	s = 0
	for i in xrange(3):
		a, b = randint(1, SIDES), randint(1, SIDES)
		s += a + b
		if a != b:
			break
		if i == 2:
			return 10
	return (pos + s) % 40
	
def play(max):
	board = [ 0 ] * 40
	board[0] = 1
	cc, ch = range(16), range(16)
	shuffle(cc), shuffle(ch)
	cci, chi = 0, 0
	pos = 0
	
	for move in xrange(max):
		pos = roll(pos)
		if pos == 30:
			pos = 10
		if pos in (2, 17, 33):
			c = cc[cci]
			cci = (cci + 1) % 16
			pos = get_new_cc_pos(c, pos)
		elif pos in (7, 22, 36):
			c = ch[chi]
			chi = (chi + 1) % 16
			pos = get_new_ch_pos(c, pos)
		board[pos] += 1
	
	return board

def normalize(board):
	s = float(sum(board))
	for i in xrange(len(board)):
		board[i] /= float(s)
	return board

def print_board(board):
	for i in xrange(11):
		print "{0:.3g}%\t".format(100 * board[i]),
	print
	for i in xrange(11, 20):
		print "{0:.3g}%{1}{2:.3g}%".format(100 * board[50 - i], "\t" * 10, 100 * board[i])
	for i in xrange(30, 19, -1):
		print "{0:.3g}%\t".format(100 * board[i]),
	print
	
def main():
	for i in xrange(1):
		board = play(500000)
		normalize(board)
		print_board(board)
main()