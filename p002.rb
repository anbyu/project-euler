a = 1
b = 2

sum = 0

while b < 4000000 do
	sum += b if b % 2 == 0

	a, b = b, a
	b += a
end

p sum
