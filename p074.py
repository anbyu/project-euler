def factorial(a):
	if a == 0 or a == 1:
		return 1
	else:
		s = 1
		for i in xrange(2, a + 1):
			s *= i
		return s
		
def gen_fs():
	fs = {}
	for i in xrange(10):
		fs[str(i)] = factorial(i)
	return fs

def next(a, fs):
	sa = str(a)
	n = 0
	for c in sa:
		n += fs[c]
	return n
	
def print_cycle(a, fs):
	l = [a]
	s = set()
	while not next(l[-1], fs) in s:
		s.add(l[-1])
		l.append(next(l[-1], fs))
	print len(l), l
	
def main():
	MAX = 10 ** 6
	TARGET = 60
	fs = gen_fs()	
	cycles = { 169: 3, 871: 2, 872: 2 }
	
	result = 0
	
	for i in xrange(MAX):
		nums = [ i ]
		while cycles.get(nums[-1], None) is None:
			n = next(nums[-1], fs)
			if nums[-1] == n:
				cycles[n] = 1
				break
			nums.append(n)
		np = cycles[nums[-1]]
		ln = len(nums)
		if ln - 1 + np == TARGET:
			result += 1
		if ln > 1:
			for j in xrange(2, ln + 1):
				cycles[nums[-j]] = np + j - 1
			
	print(result)
		
	
if __name__ == '__main__':
	#print_cycle(145, gen_fs())
	#print next(40585, gen_fs())
	main()