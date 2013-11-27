from math import log

def main():
	max = 0
	max_i = 0
	i = 1
	with open('base_exp.txt') as f:
		for line in f:
			b, e = map(int, line.split(','))
			n = e * log(b)
			if n > max:
				max = n
				max_i = i
			i += 1
		
	print max_i

if __name__ == '__main__':
	main()