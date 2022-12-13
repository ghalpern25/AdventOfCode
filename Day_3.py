f = open("Inputs/Day_3_Input.txt", "r").readlines()
priorities_sum = 0

def get_priority(item):
    priority = ord(item)
    if priority > 90:
        return priority - 96
    else:
        return priority - 38

#Part 1
for rucksack in f:
    compartment_1 = rucksack[len(rucksack) // 2:]
    compartment_2 = rucksack[:len(rucksack) // 2]
    for item in compartment_1:
        if item in compartment_2:
            priorities_sum += get_priority(item)
            break

#Part 2
group = []
badge_sum = 0
for rucksack in f:
    if len(group) == 2:
        for item in rucksack:
            if item in group[0] and item in group[1]:
                badge_sum += get_priority(item)
                group = []
                break
    else:
        group.append(rucksack)

print("Part 1:", priorities_sum)
print("Part 2:", badge_sum)