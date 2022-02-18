def two_dimention_list_pretty(target_list):
    string_return = ""
    for one_dimention_list in target_list:
        for value in one_dimention_list:
            string_return += (str(value) + " ")
        string_return += "\n"
    return string_return
