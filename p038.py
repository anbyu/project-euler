def main():
	ds = range(1, 10)
	sds = map(str, ds)
	maxp = 0
	for i in xrange(1, 10000):
		sn = str(i)
		j = 2
		while len(sn) < 10:
			sn += str(i * j)
			if len(sn) == 9:
				ok = True
				for sd in sds:
					if not sd in sn:
						ok = False
						break
				if ok:
					p = int(sn)
					if p > maxp:
						maxp = p
	return maxp
	
print main()