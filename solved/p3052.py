import sys

result_dict = {}

for i in range(0, 10):
    input_value = int(sys.stdin.readline())
    result = input_value%42
    result_dict[result] = 1

print(len(result_dict))
