def get_formulae():
	triangle = lambda n: n * (n + 1) / 2
	square = lambda n: n * n
	pentagonal = lambda n: n * (3 * n - 1) / 2
	hexagonal = lambda n: n * (2 * n - 1)
	heptagonal = lambda n: n * (5 * n - 3) / 2
	octagonal = lambda n: n * (3 * n - 2)
	return (triangle, square, pentagonal, hexagonal, heptagonal, octagonal)

def gen_numbers():
	formulae = get_formulae()
	all_numbers = []
	for f in formulae:
		numbers = []
		result = 0
		n = 0
		while result < 1000:
			n += 1
			result = f(n)
		while result < 10000:
			numbers.append(result)
			n += 1
			result = f(n)
		all_numbers.append(numbers)
	return all_numbers

def check(a, b):
	return str(a)[-2:] == str(b)[:2]

def find_next(current, lists, available):
	if len(set(current)) == 6:
		if check(current[len(current) - 1], current[0]):
			return current
		else:
			return None
	for i in available:
		new_available = set(available)
		new_available.remove(i)
		for n in lists[i]:
			if check(current[len(current) - 1], n):
				new_current = list(current)
				new_current.append(n)
				result = find_next(new_current, lists, new_available)
				if result:
					return result
	
def program():
	lists = gen_numbers()
	available = set(range(1, len(lists)))
	for n in lists[0]:
		current = [ n ]
		result = find_next(current, lists, available)
		if result:
			print result, sum(result)
	
if __name__ == '__main__':
	program()