#!/usr/bin/python3

import os

file_input = open(os.path.dirname(os.path.realpath(__file__)) + '/input', 'r')
data = file_input.readlines()

top_elfs_calories = [0, 0, 0]
elf_kcal = 0

for line in data:
    if line == '\n':
        if elf_kcal > top_elfs_calories[0]:
            top_elfs_calories[2] = top_elfs_calories[1]
            top_elfs_calories[1] = top_elfs_calories[0]
            top_elfs_calories[0] = elf_kcal
        elif elf_kcal > top_elfs_calories[1]:
            top_elfs_calories[2] = top_elfs_calories[1]
            top_elfs_calories[1] = elf_kcal
        elif elf_kcal > top_elfs_calories[2]:
            top_elfs_calories[2] = elf_kcal
        elf_kcal = 0
    else:
        elf_kcal = elf_kcal + int(line.strip('\n'))

total = sum(top_elfs_calories)

file_result = open(os.path.dirname(os.path.realpath(__file__)) + '/result.part-2', 'w')
file_result.write('Answer for part 2 is: ' + str(total) + '\n')