input = ''
with open('day6_input.txt') as file:
    input = file.readline()

# input = 'nppdvjthqldpwncqszvftbrmjlhg'

# Part 1
idx = 0
packet_marker = ''

for idx in range(len(input) - 3):
    packet_marker = input[idx:idx + 4]
    is_sop_marker = len(set(packet_marker)) == 4
    if is_sop_marker:
        print(packet_marker)
        print(f'First marker after character {idx + 4}')
        break

# Part 2
idx = 0
msg_marker = ''

for idx in range(len(input) - 3):
    msg_marker = input[idx:idx + 14]
    is_som_marker = len(set(msg_marker)) == 14
    if is_som_marker:
        print(msg_marker)
        print(f'First marker after character {idx + 14}')
        break