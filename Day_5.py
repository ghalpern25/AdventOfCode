f = open("Inputs/Day_5_Input.txt", "r").readlines()

crate_stacks_1 = [[] for _ in range(len(f[0]) // 4)]
crate_stacks_2 = [[] for _ in range(len(f[0]) // 4)]

line_num = 0
for line in f:
    if '1' in line:
        break

    for i in range(1, len(line), 4):
        if line[i] != ' ':
            crate_stacks_1[i // 4].insert(0, line[i])
            crate_stacks_2[i // 4].insert(0, line[i])
    line_num += 1

#part 1
for line in f[10:]:
    instructions = line.split(' ')
    for i in range(int(instructions[1])):
        crate_stacks_1[int(instructions[5]) - 1].append(crate_stacks_1[int(instructions[3]) - 1].pop())

top_1 = ""
for stack in crate_stacks_1:
    top_1 += stack[-1]

#part 2
for line in f[10:]:
    instructions = line.split(' ')

    moving_stack = crate_stacks_2[int(instructions[3]) - 1][-int(instructions[1]):]
    crate_stacks_2[int(instructions[3]) - 1] = crate_stacks_2[int(instructions[3]) - 1][:-int(instructions[1])]
    crate_stacks_2[int(instructions[5]) - 1] += moving_stack

top_2 = ""
for stack in crate_stacks_2:
    top_2 += stack[-1]

print("Part 1:", top_1)
print("Part 2:", top_2)