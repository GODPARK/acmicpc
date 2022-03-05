
def calc(number_list, index, result, target, answer_list):
    if len(number_list) <= index:
        if target == result:
            answer_list.append(1)
        return 0
    calc(number_list, index+1, result+number_list[index],target, answer_list)
    calc(number_list, index+1, result-number_list[index], target, answer_list)

def solution(numbers, target):
    a_list = []
    calc(numbers, 1, numbers[0], target, a_list)
    b_list = []
    calc(numbers, 1, -numbers[0], target, b_list)
    return len(a_list) + len(b_list)
