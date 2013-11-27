def common_words():
	words = [ 'the', 'be', 'to', 'of', 'and', 'in', 'that', 'have' ]
	for i in xrange(len(words)):
		words[i] = map(ord, list(words[i]))
	return words
	
def decipher(ciphered, key):
	deciphered = list(ciphered)
	lc = len(ciphered)
	lk = len(key)
	i = 0
	while i < lc:
		deciphered[i] ^= key[i % lk]
		i += 1
	return deciphered

def nums2txt(nums):
	txt = list(nums)
	txt = map(chr, txt)
	return ''.join(txt)
	
def program():
	with open('cipher1.txt') as f:
		ciphered = map(int, f.read().strip().split(','))
	words = common_words()
	a, b = ord('a'), ord('z') + 1
	for i in xrange(a, b):
		for j in xrange(a, b):
			for k in xrange(a, b):
				deciphered = decipher(ciphered, [i, j, k])
				c = 0
				for word in words:
					c += count(word, deciphered)
				if c > 30:
					print nums2txt(deciphered)
					print nums2txt([i, j, k])
					print sum(deciphered), i, j, k
				
def count(seq, bigger):
	c = 0
	si = 0
	while len(bigger) > 0:
		try:
			si = bigger.index(seq[0])
		except ValueError:
			return c
		ls = len(seq)
		found = True
		for i in xrange(1, ls):
			if bigger[si + i] != seq[i]:
				found = False
				break
		if found:
			c += 1
		bigger = bigger[si + 1:]
	return c
		

def test():
	print count([1,2,3], [0, 1, 2, 3, 1, 1, 2, 3])

if __name__ == '__main__':
	program()
	#test()
	