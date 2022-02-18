def quick_sort(array):
    return sort(array, 0, len(array) -1)


def sort(array, start, end):
    if end <= start:
        return
    index = partition(array, start, end)
    sort(array, start, index - 1)
    sort(array, index, end)


def partition(array, start, end):
    pivot = array[(start + end) // 2]
    while start <= end:
        while array[start] < pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start <= end:
            array[start], array[end] = array[end], array[start]
            start, end = start + 1, end - 1
    return start


#-------------------------
test_arr = [
    5, 4, 3, 2, 1, 2,3, 4,5, -1, -2, 100, 0
]


quick_sort(test_arr)
print(test_arr)
