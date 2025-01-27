streams = int(input())
flows = []

for i in range(streams):
    flows.append(int(input(f"Give the value of the flow of stream number {i}: ")))

instructions = []
user = 0
while user != 77:
    split = []
    join = []
    user = int(input("Give inst: "))
    if user == 99:
        split.append(user)
        for _ in range(2):
            splitting_input = int(input())
            split.append(splitting_input)
        instructions.append(split)
    elif user == 88:
        join.append(user)
        joining_input = int(input())
        join.append(joining_input)
        instructions.append(join)

for i in range(len(instructions) - 1):
    if instructions[i][0] == 99:
        flows.insert((instructions[i][1]), (flows[instructions[i][1] - 1] - round(flows[instructions[i][1] - 1] * (instructions[i][2]/100))))
        flows[instructions[i][1] - 1] = round(flows[instructions[i][1] - 1] * (instructions[i][2]/100))
    elif instructions[i][0] == 88:
        flows[instructions[i][1] - 1] += flows[instructions[i][1]]
        del flows[instructions[i][1]]

output = ""
for data in flows:
    output += str(data) + " "

print(output)
        
