rucksacks = []

with open('day3_input.txt') as file:
    for line in file:
        rucksacks.append(line.rstrip())

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = {}
for idx, char in enumerate(ascii_letters):
    priority[char] = idx + 1

# rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
# 'ttgJtRGJQctTZtZT',
# 'CrZsJsPPZsGzwwsLwLmpwMDw']

# Part 1
total = 0
for rucksack in rucksacks:
    half = int(len(rucksack) / 2)
    left = rucksack[:half]
    right = rucksack[half:]
    for item in left:
        if item in right:
            total += priority[item]
            break
    half = 0

print(total)

# Part 2
total = 0
group = []
for idx, rucksack in enumerate(rucksacks):
    if (idx + 1) % 3 != 0:
        group.append(rucksack)
    else:
        group.append(rucksack)
        least_item = min([len(rucksack) for rucksack in group])
        for item in group[0]:
            if item in group[1] and item in group[2]:
                total += priority[item]
                break
        group.clear()

print(total)