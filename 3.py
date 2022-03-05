# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def abs(a):
    if a >= 0:
        return a
    else:
        return a * -1


def solution(A):
    # write your code in Python 3.6
    number_dict = {}

    positive_count = 0
    negative_count = 0

    for a in A:
        if a > 0:
            positive_count += 1
        elif a < 0:
            negative_count += 1

        number_dict[a] = a * -1

    if positive_count == len(A) or negative_count == len(A):
        return 0

    k = -1000000001
    for a in A:
        if a in number_dict and -1 * a in number_dict:
            if k < a:
                k = a

    if k == -1000000001:
        return 0

    return abs(k)

