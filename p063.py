def program():
	count = 9
	p = 2
	
	while p < 100:
		b = 2
		ln = 1
		while ln <= p:
			n = b ** p
			ln = len(str(n))
			if ln == p:
				count += 1
			b += 1		
		p += 1
	print count
		
if __name__ == '__main__':
	program()
