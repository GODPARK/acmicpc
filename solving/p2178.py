import sys

input_nm = str(sys.stdin.readline()).split(" ")
n = int(input_nm[0])
m = int(input_nm[1])

map_list = []
count_list = []

def two_dimention_list_pretty(target_list):
    string_return = ""
    for one_dimention_list in target_list:
        for value in one_dimention_list:
            string_return += (str(value) + " ")
        string_return += "\n"
    return string_return

def search_map(x, y ,count, map):
    if x >= 0 and x <= m-1 and y >= 0 and y <= n-1 and map[y][x] != 0 and map[y][x] != 2:
        if x == (m-1) and y == (n-1):
            count_list.append(count)

        map[y][x] = 2
        print(two_dimention_list_pretty(map))

        search_map(x + 1, y, count + 1, map)
        search_map(x - 1, y, count + 1, map)
        search_map(x, y+1, count + 1, map)
        search_map(x, y-1, count + 1, map)
    else:
        return


for index in range(0, n):
    row_str = str(sys.stdin.readline()).replace("\n", '')
    input_row = [ int(x) for x in row_str]
    map_list.append(input_row)


print(map_list)
search_map(0,0,0, [x for x in map_list])
print(count_list)
