import io
import os
import re

def make_joltage(*parts):
    return int(''.join(str(p) for p in parts))

def find_largest(string):
    largest = 0
    largest_indx = 0
    for index, char in enumerate(string):
        current_digit = int(char)
        if current_digit > largest:
            largest = current_digit
            largest_indx = index
    return largest_indx, largest

def find_largest_joltage(bank):
    digits = ''.join(ch for ch in str(bank) if ch.isdigit())
    indx, largest = find_largest(digits[:-1])
    indx, largest2 = find_largest(digits[indx+1:-1])
    if(int(digits[-1]) > int(largest2)):
        return make_joltage(largest, digits[-1])
    return make_joltage(largest, largest2)

def find_largest_joltage_part2(bank, n=12):
    digits = ''.join(ch for ch in str(bank) if ch.isdigit())
    to_remove = len(digits) - n
    activated = []
    for d in digits:
        while activated and activated[-1] < d and to_remove > 0:
            activated.pop()
            to_remove -= 1
        activated.append(d)
    return make_joltage(*activated[:n])

if __name__ == "__main__":
    joltage = 0
    with open("day3.txt", 'r') as fh:
        buf = []
        size = os.fstat(fh.fileno()).st_size
        while fh.tell() < size:
            for line in fh:
                #jolt = find_largest_joltage(line)
                jolt = find_largest_joltage_part2(line)
                joltage += jolt
                print(f"bank jolt: {jolt}")

    print(joltage)