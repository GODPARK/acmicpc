
def max_value_in_list (target_list):
    if target_list:
        max_value = target_list[0]
        for value in target_list:
            if max_value <= value:
                max_value = value
        return max_value
    else:
        # list is empty
        return 0


def max_value(a, b):
    if a >= b:
        return a
    else:
        return b


print(max_value_in_list([1, 2, 5, 3,2,1, 2, 22, 34,22,66,-1,-3,-4,5]))