import sys

def group_string_checker(word):

    duplicate_dict = {}

    for char in word:
        if char in duplicate_dict:
            if char != before_char:
                return False
        else:
            duplicate_dict[char] = True
        before_char = char

    return True


num = int(sys.stdin.readline())
result_num = 0

for index in range(0, num):
    seperated_str = str(sys.stdin.readline()).replace("\n", '')
    if group_string_checker(seperated_str):
        result_num += 1

print(result_num)
