# Day 1: Sonar Sweep

with open("input.txt") as file:
    depth_list = file.readlines()

depth_increased_count = 0
prev_sum = 0

for i, line in enumerate(depth_list):
    if i >= (len(depth_list) - 3):
        break
    sum = 0
    for line in depth_list[i:i+3]:
        depth = int(line)
        sum = sum + depth

    # Check if sum depth measurements increased from the previous sum of measurements
    if sum > prev_sum:
        depth_increased_count += 1

    prev_sum = sum

print(depth_increased_count)