def tens(n, numbers):
	if n < 21:
		print numbers[n],
		return len(numbers[n])
	elif n < 100:
		print numbers[n / 10 + 18], numbers[n % 10],
		return len(numbers[n / 10 + 18] + numbers[n % 10])

def f():
	numbers = [ '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]
	
	total = 0
	
	for n in xrange(1, 1000):
		print n,
		if n < 100:
			r = tens(n, numbers)
			print r
			total += r
		else:
			if n % 100 == 0:
				print numbers[n / 100], 'hundred',
				r = len(numbers[n / 100] + 'hundred') + tens(n % 100, numbers)
				print r
				total += r
			else:
				print numbers[n / 100], 'hundred', 'and', 
				r = len(numbers[n / 100] + 'hundred' + 'and') + tens(n % 100, numbers)
				print r
				total += r
	
	print 1000, 'one thousand'
	total += len('onethousand')
	
	return total
print f()