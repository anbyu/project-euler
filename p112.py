def is_bouncy(n):
	inc, dec = False, False
	cn = n
	
	last = cn % 10
	cn /= 10
	while cn != 0:
		curr = cn % 10
		if curr > last:
			inc = True
		elif curr < last:
			dec = True
		if inc and dec:
			return True
		last = curr
		cn /= 10
		
	return False

def main():
	START = 21780
	TARGET = 99
	p = 90
	
	bn = START * p / 100
	c = START
	
	while p != TARGET:
		c += 1
		if is_bouncy(c):
			bn += 1
		p = 100 * bn / c
	print bn, c, p
	
if __name__ == '__main__':
	main()