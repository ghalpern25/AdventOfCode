f = open("2-input.txt")
score_1 = 0
score_2 = 0

def calc_score(opponent, me):
    round_score = 0
    round_score += me - 64
    if opponent == ord('C') and me == ord('A'):
        round_score += 6
    elif opponent == ord('A') and me == ord('C'):
        pass
    elif me > opponent:
        round_score += 6
    elif me == opponent:
        round_score += 3
    return round_score

def part_1(opponent, me):
    return calc_score(ord(opponent), ord(me) - 23)

def part_2(opponent, me):
    if me == 'Y':
        me = opponent
    if me == 'X':
        me = chr(ord(opponent) - 1)
        if me == '@':
            me = 'C'
    if me == 'Z':
        me = chr(ord(opponent) + 1)
        if me == 'D':
            me = 'A'
    
    return calc_score(ord(opponent), ord(me))



for line in f:
    opponent, me = line[:3].split(' ') #substring to remove newline
    score_1 += part_1(opponent, me)
    score_2 += part_2(opponent, me)

print("Round 1:", score_1)
print("Round 2:", score_2)
