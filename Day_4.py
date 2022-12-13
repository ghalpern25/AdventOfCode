f = open("Inputs/Day_4_Input.txt", "r").readlines()

total_overlaps = 0
partial_overlaps = 0
for line in f:
    pair = line.split(",")
    left = [int(x) for x in pair[0].split("-")]
    right = [int(x) for x in pair[1].split("-")]
    if (left[0] >= right[0] and left[1] <= right[1]) or (left[0] <= right[0] and left[1] >= right[1]):
        total_overlaps += 1

    if left[0] in range(right[0], right[1] + 1) or left[1] in range(right[0], right[1] + 1) or right[0] in range(left[0], left[1] + 1) or right[1] in range(left[0], left[1] + 1):
        partial_overlaps += 1
    

print("Total overlaps:", total_overlaps)
print("Partial overlaps:", partial_overlaps)