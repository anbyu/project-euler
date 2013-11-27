max = 20

i = 2
result = 1

while i <= max do
    j = 2
    while result % i != 0 do
        result /= (j - 1)
        result *= j
        j += 1
    end
    puts i.to_s + ' ' + result.to_s
    i += 1
end

puts result