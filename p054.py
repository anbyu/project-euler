from sys import stdin

class Card:
	def __init__(self, code):
		self.v, self.c = self.parse(code)
		
	def parse(self, code):
		d = { '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }
		v = d[code[0]]
		c = code[1]
		return v, c

def count_cards(cards):
	d = dict(zip(range(2, 15), [0] * 13))
	for card in cards:
		d[card.v] += 1
	s = sorted(d.items(), key=lambda x: x[1], reverse=True)
	if s[0][1] == 4:
		print "four of a kind"
		return 5000 + s[0][0]
	elif s[0][1] == 3:
		if s[1][1] == 2:
			print "full house"
			return 4000 + s[0][0]
		else:
			print "three of a kind"
			return 3000 + s[0][0]
	elif s[0][1] == 2:
		if s[1][1] == 2:
			print "two pairs"
			return 2000 + max(s[0][0], s[1][0])
		else:
			print "one pair"
			return 1000 + s[0][0]
	else:
		print "high card"
		return 0
		
def check_straight(cards):
	for i in xrange(1, len(cards)):
		if cards[i].v - cards[i-1].v != 1:
			return False
	return True
	
def check_flush(cards):
	c = cards[0].c
	for i in xrange(1, len(cards)):
		if cards[i].c != c:
			return False
	return True

def check_hand(cards):
	highest = cards[len(cards) - 1].v
	has_straight = check_straight(cards)
	has_flush = check_flush(cards)
	
	if has_straight and has_flush:
		print "straight flush"
		return 6900 + highest
	elif has_flush:
		print "flush"
		return 3600 + highest
	elif has_straight:
		print "straight"
		return 3300 + highest
	
	points = count_cards(cards)
	if points == 0:
		points += highest
	return points
		
	
def game(s):
	codes = s.split()
	cards = []
	for code in codes:
		cards.append(Card(code))
	cards_p1 = sorted(cards[:5], key=lambda c: c.v)
	cards_p2 = sorted(cards[5:], key=lambda c: c.v)
	
	points1 = check_hand(cards_p1)
	points2 = check_hand(cards_p2)
	
	if points1 > points2:
		return (1, 0)
	elif points1 < points2:
		return (0, 1)
	else:
		return (0, 0)
		
def poker():
	p1, p2 = 0, 0
	for line in stdin:
		result = game(line)
		print line, result
		p1 += result[0]
		p2 += result[1]
	print p1, p2
	
if __name__ == '__main__':
	poker()