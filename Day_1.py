max_cals = 0
max_2 = 0
max_3 = 0
cals = 0
f = open("1-input.txt", "r")
for line in f:
    if line != "\n":
        cals += int(line)
    else:
        if cals > max_cals:
            max_3 = max_2
            max_2 = max_cals
            max_cals = cals
        elif cals > max_2:
            max_3 = max_2
            max_2 = cals
        elif cals > max_3:
            max_3 = cals
        cals = 0

print(max_cals + max_2 + max_3)
f.close()