notes = open("Inputs/Day_11_Input.txt", "r").readlines()


#Dictionary layout:
#monkeys {
#   0: {
#       items: [x, y, z],
#       operation: "a * b",
#       test_divisor: 17,
#       test_decision: {
#           True: 3,
#           False: 1
#           }
#       }
# }

monkeys = {}

def setup():
    num_lines = len(notes)
    num_monkeys = (num_lines + 1) // 7
    line_iterator = iter(notes)

    while (num_monkeys > 0):
        current_line = next(line_iterator)
        monkey_num = int(current_line[7:-2])
        monkeys[monkey_num] = {"items":[]}

        current_line = next(line_iterator)
        items = current_line[18:].split(",")
        for item in items:
            monkeys[monkey_num]["items"].append(int(item.strip()))

        monkeys[monkey_num]["operation"] = next(line_iterator)[19:-1]

        monkeys[monkey_num]["test"] = int(next(line_iterator)[21:-1])
        
        monkeys[monkey_num]["decision"] = {}
        
        monkeys[monkey_num]["decision"][True] = int(next(line_iterator)[29:-1])
        
        monkeys[monkey_num]["decision"][False] = int(next(line_iterator)[30:].strip())

        monkeys[monkey_num]["inspections"] = 0

        num_monkeys -= 1
        if num_monkeys > 0: next(line_iterator)
    

setup()


for i in range(20):
    for monkey in monkeys:
        for item in monkeys[monkey]["items"]:
            old = item
            new = eval(monkeys[monkey]["operation"]) // 3
            pass_to = monkeys[monkey]["decision"][new % monkeys[monkey]["test"] == 0]
            monkeys[pass_to]["items"].append(new)
        
        monkeys[monkey]["inspections"] = monkeys[monkey]["inspections"] + len(monkeys[monkey]["items"])
        monkeys[monkey]["items"] = []

    print("\nAfter Round", i + 1, ":")
    for monkey in monkeys:
        print("Monkey", monkey, ":", monkeys[monkey]["items"])

max_1 = 0
max_2 = 0
for monkey in monkeys:
    inspections = monkeys[monkey]["inspections"]
    if inspections > max_1:
        max_2 = max_1
        max_1 = inspections
    elif inspections > max_2:
        max_2 = inspections

monkey_business = max_1 * max_2
print(monkey_business)
