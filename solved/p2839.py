import sys
import math

input_kg = int(sys.stdin.readline())

try_list = []

def seperate(kg, count):
    if kg > 0:
        seperate(kg-3, count+1)
        seperate(kg-5, count+1)
    elif kg == 0:
        try_list.append(count)
        return
    else:
        return

def list_min():
    if len(try_list) > 0:
        return min(try_list)
    else:
        return -1

if input_kg > 16:
    value = input_kg - 16
    bag5 = math.floor(value / 5)
    input_kg = input_kg - bag5*5
    seperate(input_kg, 0)
    print(bag5 + list_min())
else:
    seperate(input_kg, 0)
    print(list_min())