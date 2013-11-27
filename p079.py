def main():
	with open('keylog.txt') as f:
		ints = map(int, f.readlines())
		
	strs = map(str, ints)
	lsts = map(list, strs)
	
	sets = [set() for i in range(10)]
	
	for i in range(10):
		si = str(i)
		for lst in lsts:
			for j in range(3):
				if lst[j] == si:
					sets[i] = sets[i].union(lst[0:j])
	
	stats = []
	for i in range(10):
		s = sets[i]
		ls = len(s)
		if ls > 0:
			stats.append((i, ls))
	
	stats.sort(key=lambda t: t[1])
	
	code = map(str, [t[0] for t in stats])
	
	return ''.join(code)

print main()