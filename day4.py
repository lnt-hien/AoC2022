total1 = 0
total2 = 0
with open('day4_input.txt') as file:
    for line in file:
        line = line.rstrip()
        first, second = line.split(',')
        s1, e1 = map(int, first.split('-'))
        s2, e2 = map(int, second.split('-'))

        # Part 1
        if s1 <= s2 and e2 <= e1 or s1 >= s2 and e2 >= e1:
            total1 += 1

        # Part 2
        if s1 <= s2 and e2 <= e1 or s1 >= s2 and e2 >= e1 or s1 <= e2 and s2 <= e1:
            total2 += 1

print(total1)
print(total2)