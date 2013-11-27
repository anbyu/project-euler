r2ad = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
a2rd = dict((v, k) for k, v in r2ad.items())

def roman2arabic(roman):
	arabic = 0
	lc = len(roman)
	for i in xrange(lc):
		curr = r2ad[roman[i]]
		if i + 1 < lc and curr < r2ad[roman[i + 1]]:
			arabic -= curr
		else:
			arabic += curr
	return arabic
	
def arabic2roman(arabic):
	numbers = sorted(r2ad.values(), reverse = True)
	ln = len(numbers)
	roman = []
	for i in xrange(ln):
		n = numbers[i]
		while n <= arabic:
			arabic -= n
			roman.append(a2rd[n])
		for j in xrange(ln - 1, i, -1):
			m = numbers[j]
			if not m in (1, 10, 100) or n / m == 2 or n / m > 10:
				continue
			if n - m <= arabic:
				arabic -= n - m
				roman.append(a2rd[m])
				roman.append(a2rd[n])
	
	return ''.join(roman)
	
def process_roman(file):
	total_diff = 0
	for line in file:
		roman = line.strip()
		arabic = roman2arabic(roman)
		new_roman = arabic2roman(arabic)
		diff = len(roman) - len(new_roman)
		diff2 = len(roman) - len(shorten(roman))
		if diff != diff2:
			print roman, '\t', arabic, '\t', new_roman, '\t', shorten(roman)
			#raise ValueError
		total_diff += diff
	return total_diff

def shorten(roman):
	shortened = roman
	replacements = [
		('VIIII', 'IX'),
		('IIII', 'IV'),
		('LXXXX', 'XC'),
		('XXXX', 'XL'),
		('DCCCC', 'CM'),
		('CCCC', 'CD')
	]
	for old, new in replacements:
		shortened = shortened.replace(old, new)
	return shortened
	
def program():
	with open('roman.txt') as f:
		print process_roman(f)

def test():
	print arabic2roman(501)
		
if __name__ == '__main__':
	program()
	#test()