villages = int(input("Give number of villages: "))
positions = []

for i in range(villages):
    positions.append(int(input(f"Give position of village {i} ")))
positions.sort()

sizes = []
for i in range(villages - 2):
    left_size = (positions[i+1] - positions[i])/2
    right_size = (positions[i+2] - positions[i+1])/2

    sizes.append((a+b))

print(min(sizes))
