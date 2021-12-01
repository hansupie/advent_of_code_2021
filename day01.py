# Day 1: Sonar Sweep

with open("input.txt") as file:
    depth_list = file.readlines()

prev_depth = 0
depth_increased_count = 0

for i, line in enumerate(depth_list):
    depth = int(line)
    # Check if depth measurement increased from the previous measurement
    if i != 0 and depth > prev_depth:
        depth_increased_count += 1
    prev_depth = depth

print(depth_increased_count)