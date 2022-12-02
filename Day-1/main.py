#!/usr/bin/python3

import os

file_input = open(os.path.dirname(os.path.realpath(__file__)) + '/input', 'r')
data = file_input.readlines()

max = 0
sum = 0

for line in data:
    if line == '\n':
        if sum > max:
            max = sum
        sum = 0
    else:
        sum = sum + int(line.strip('\n'))

file_result = open(os.path.dirname(os.path.realpath(__file__)) + '/result', 'w')
file_result.write('Answer is: ' + str(max) + '\n')