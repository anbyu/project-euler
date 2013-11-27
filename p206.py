def check(n):
	sn = str(n)
	return sn[-3] == '9' and sn[-5] == '8' and sn[-7] == '7' \
		and sn[-9] == '6' and sn[-11] == '5' and sn[-13] == '4' \
		and sn[-15] == '3' and sn[-17] == '2' and sn[-19] == '1'

def main():
	mi = int(1020304050607080900 ** 0.5 + 1)
	ma = int(1929394959697989990 ** 0.5 + 1)
	
	i = mi
	while i < ma:
		if i % 100 == 30 or i % 100 == 70:
			break
		i += 1
		
	while i < ma:
		c = False
		if i % 100 == 30:
			a = 40
		elif i % 100 == 70:
			a = 60
		if(check(i * i)):
			print(i)
			return
		i += a

if __name__ == '__main__':
	main()
