
def swap_value_in_list(target_list, first_index, second_index):
    temp_value = target_list[first_index]
    target_list[first_index] = target_list[second_index]
    target_list[second_index] = temp_value
    return target_list

