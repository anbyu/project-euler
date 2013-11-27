max = 100

squared_sum = ((1 + max) * max / 2) ** 2

sum_squares = 0
max.times do |i|
    sum_squares += (i+1) ** 2
end

puts squared_sum - sum_squares
