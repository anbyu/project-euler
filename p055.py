def isp(n):
	sn = str(n)
	return sn == sn[::-1]

def raa(n):
	sn = str(n)
	return n + int(sn[::-1])
	
def main():
	count = 0
	for n in xrange(1, 10001):
		isl = True
		for j in xrange(50):
			n = raa(n)
			if isp(n):
				isl = False
				break
		if isl:
			count += 1
	return count
	
print main()