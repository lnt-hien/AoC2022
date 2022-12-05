list_cal = []
max_cal = 0
current = 0

with open("day1_input.txt") as file:
    for line in file:
        if line.rstrip() == "":
            if current > max_cal:
                max_cal = current
            list_cal.append(current)
            current = 0
        else:
            current += int(line.rstrip())

# Part 1
print(max_cal)
# Part 2
print(sum(sorted(list_cal, reverse=True)[:3]))
