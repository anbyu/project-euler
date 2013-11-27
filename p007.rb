max = 1000000

primes = (2..max).to_a

i = 0
while i < primes.length do
    j = i
    if primes[i] != nil then
        delta = primes[i]
        
        j += delta
        while j < primes.length do
            primes[j] = nil
            j += primes[i]
        end
    end
    i += 1
end

primes.compact!

puts primes[10000]