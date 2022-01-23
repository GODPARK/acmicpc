import sys

input_str = str(sys.stdin.readline())

result_list = input_str.split(" ")
result_validate_list = [ value for value in result_list if value and value != '\n' ]

print(len(result_validate_list))