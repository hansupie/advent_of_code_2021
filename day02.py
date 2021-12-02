# Day 2: Dive!

with open("input2.txt") as file:
    depth_list = file.readlines()

vertical_pos = 0
horizontal_pos = 0

for line in depth_list:
    command = line.split()[0]
    amount = int(line.split()[1])

    if command == "forward":
        horizontal_pos += amount

    if command == "down":
        vertical_pos += amount
    
    if command == "up":
        vertical_pos -= amount

print(vertical_pos)
print(horizontal_pos)
print(vertical_pos * horizontal_pos)
