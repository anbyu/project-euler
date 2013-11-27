from common import sieve

def main():
	MAX = 5 * 10 ** 7
	
	d = sieve(int(MAX ** 0.5) + 1)
	t = sieve(int(MAX ** (1.0/3)) + 1)
	q = sieve(int(MAX ** (0.25)) + 1)
	
	numbers = set()
	for qi in q:
		for ti in t:
			for di in d:
				n = qi * qi * qi * qi + ti * ti * ti + di * di
				if n < MAX:
					numbers.add(n)
				else:
					break
	print(len(numbers))

if __name__ == '__main__':
	main()