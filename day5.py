moves = []

with open('day5_input.txt') as file:
    for line in file:
        line = line.rstrip().split(' ')
        moves.append(line)

moves = moves[10:]

stacks = [
    ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
    ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
    ['C', 'B', 'S', 'N', 'W'],
    ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
    ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
    ['J', 'V', 'T', 'W', 'M', 'N'],
    ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
    ['B', 'D', 'Z'],
    ['M', 'N', 'Z', 'W']
]

import copy

stacks1 = copy.deepcopy(stacks)
stacks2 = copy.deepcopy(stacks)
for move in moves:
    start = int(move[3]) - 1
    to = int(move[5]) - 1
    crate_number = int(move[1])

    # Part 1
    for crate in range(crate_number):
        stacks1[to].append(stacks1[start].pop(-1))

    # Part 2
    for crate in range(crate_number, 0, -1):
        stacks2[to].append(stacks2[start].pop(-crate))

top_crates = ""
for stack in stacks1:
    top_crates += stack[-1]
print(top_crates)

top_crates = ""
for stack in stacks2:
    top_crates += stack[-1]
print(top_crates)