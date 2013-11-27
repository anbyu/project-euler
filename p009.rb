c = 0
catch (:done) do
    while c < 1000
        b = 0
        while b < c
            a = 0
            while a < b
                if a + b + c == 1000 and a*a + b*b == c*c then
                    puts a*b*c 
                    throw :done
                end
                a += 1
            end
            b += 1
        end
        c += 1
    end
end
                