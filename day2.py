rounds = []

with open("day2_input.txt") as file:
    for line in file:
        rounds.append(line.rstrip().split(" "))

score = 0
# Part 1
# Naive approach
for r in rounds:
    if r[1] == 'X':
        score += 1
    if r[1] == 'Y':
        score += 2
    if r[1] == 'Z':
        score += 3

    if r[0] == 'A' and r[1] == 'Y' or r[0] == 'B' and r[1] == 'Z' or r[0] == 'C' and r[1] == 'X':
        score += 6
    if r[0] == 'A' and r[1] == 'X' or r[0] == 'B' and r[1] == 'Y' or r[0] == 'C' and r[1] == 'Z':
        score += 3
    if r[0] == 'A' and r[1] == 'Z' or r[0] == 'B' and r[1] == 'X' or r[0] == 'C' and r[1] == 'Y':
        score += 0


print(score)

# Part 2
# Naive approach
score = 0
for r in rounds:
    if r[1] == 'X':
        score += 0
    if r[1] == 'Y':
        score += 3
    if r[1] == 'Z':
        score += 6

    if r[0] == 'A' and r[1] == 'Y' or r[0] == 'B' and r[1] == 'X' or r[0] == 'C' and r[1] == 'Z':
        score += 1
    if r[0] == 'A' and r[1] == 'X' or r[0] == 'B' and r[1] == 'Z' or r[0] == 'C' and r[1] == 'Y':
        score += 3
    if r[0] == 'A' and r[1] == 'Z' or r[0] == 'B' and r[1] == 'Y' or r[0] == 'C' and r[1] == 'X':
        score += 2


print(score)
