# Day 3: Binary Diagnostic

def list_to_string(s):
    string_ints = [str(int) for int in s]
    str_of_ints = ""
    return (str_of_ints.join(string_ints))

def binary_to_decimal(n):
    return int(n,2)

def find_most_common(list, pos):
    zero_count = 0
    one_count = 0

    for bin in list:
        if int(bin[pos]) == 0:
            zero_count += 1
        else:
            one_count += 1
    
    if zero_count > one_count:
        return 0
    elif one_count > zero_count:
        return 1
    else:
        return 1

def find_least_common(list, pos):
    common = find_most_common(list, pos)
    least_common = 1 if common == 0 else 0
    return least_common

def find_oxygen_rating(binary_list, pos):
    if len(binary_list) == 1:
        return binary_list
    
    else:
        common = find_most_common(binary_list, pos)
        new_list = []

        for binary in binary_list:
            bin_list = []
            bin_list[:0] = binary
            bin_int = int(bin_list[pos])
            if bin_int == common:
                new_list.append(binary)

        return find_oxygen_rating(new_list, pos+1)

def find_co2_rating(binary_list, pos):
    if len(binary_list) == 1:
        return binary_list
    else:
        least_common = find_least_common(binary_list, pos)
        new_list = []

        for binary in binary_list:
            if int(binary[pos]) == least_common:
                new_list.append(binary)
        return find_co2_rating(new_list, pos+1)

def find_gamma_rate(list):
    pos = 0
    while pos < len(list[0]):
        most_common = find_most_common(list, pos)
        gamma_rate.append(most_common)
        pos += 1
    return gamma_rate

def find_epsilon_rate(list):
    pos = 0
    while pos < len(list[0]):
        least_common = find_least_common(list, pos)
        epsilon_rate.append(least_common)
        pos += 1
    return epsilon_rate

with open("input3.txt") as file:
    diagnostic = file.readlines()

stripped_diag = []
for line in diagnostic:
    stripped_line = line.strip()
    stripped_diag.append(stripped_line)

gamma_rate = []
gamma_rate = find_gamma_rate(stripped_diag)
gamma_str = list_to_string(gamma_rate)
gamma_dec = binary_to_decimal(gamma_str)

epsilon_rate = []
epsilon_rate = find_epsilon_rate(stripped_diag)
epsilon_str = list_to_string(epsilon_rate)
epsilon_dec = binary_to_decimal(epsilon_str)

oxygen = find_oxygen_rating(stripped_diag, 0)
co2 = find_co2_rating(stripped_diag, 0)

oxygen_str = list_to_string(oxygen)
co2_str = list_to_string(co2)
oxygen_dec = binary_to_decimal(oxygen_str)
co2_dec = binary_to_decimal(co2_str)

print("The gamma rate is ", gamma_dec)
print("The epsilon rate is ", epsilon_dec)
print("The power consumpion is ", gamma_dec * epsilon_dec)

print("The oxygen generator rating is ", oxygen_dec)
print("The CO2 scrubber rating is ", co2_dec)
print("The life support rating is ", oxygen_dec * co2_dec)