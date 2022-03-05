import sys
from collections import deque

class Dangi:

    size_square = 0
    apart_list = []
    dangi_num = 1
    dan_stat = {}
    visit_list = []

    def __init__(self):
        pass

    def get_size_square(self):
        return self.size_square

    def get_apart_list(self):
        return self.apart_list

    def get_apart_list_by_cord(self, x, y):
        return self.apart_list[y][x]

    def get_dan_stat(self):
        return self.dan_stat

    def print_pretty_apart_list(self):
        for row in self.apart_list:
            print(row)
        print("\n")

    def input_value(self):
        self.size_square = int(sys.stdin.readline())
        for i in range(0, self.size_square):
            row_list = []
            visit_row_list = []
            for col in sys.stdin.readline():
                if col != '\n':
                    row_list.append(int(col))
                    visit_row_list.append(0)
            self.visit_list.append(visit_row_list)
            self.apart_list.append(row_list)

    def is_not_visit(self, y, x):
        if self.visit_list[y][x] == 1:
            return False
        else:
            return True

    def visit_mark(self, y, x):
        self.visit_list[y][x] = 1

    def search_dan(self, x, y):
        deq = deque()
        if self.apart_list[y][x] == 1:
            deq.append([y, x])
            self.dangi_num += 1
            self.dan_stat[self.dangi_num] = 0

        while len(deq) > 0:
            cordi = deq.popleft()
            if self.is_not_visit(cordi[0], cordi[1]):
                self.apart_list[cordi[0]][cordi[1]] = self.dangi_num

                if self.dangi_num in self.dan_stat:
                    self.dan_stat[self.dangi_num] += 1

                self.visit_mark(cordi[0], cordi[1])

                if cordi[0] -1 >= 0:
                    if self.apart_list[cordi[0]-1][cordi[1]] == 1 and self.is_not_visit(cordi[0]-1, cordi[1]):
                        deq.append([cordi[0]-1, cordi[1]])
                if cordi[1] - 1 >= 0:
                     if self.apart_list[cordi[0]][cordi[1]-1] == 1 and self.is_not_visit(cordi[0], cordi[1]-1):
                        deq.append([cordi[0], cordi[1]-1])
                if cordi[0] + 1 < self.size_square:
                    if self.apart_list[cordi[0]+1][cordi[1]] == 1 and self.is_not_visit(cordi[0]+1, cordi[1]):
                        deq.append([cordi[0]+1, cordi[1]])
                if cordi[1] + 1 < self.size_square:
                    if self.apart_list[cordi[0]][cordi[1]+1] == 1 and self.is_not_visit(cordi[0], cordi[1]+1):
                        deq.append([cordi[0], cordi[1]+1])





dan = Dangi()
dan.input_value()
size_square = dan.get_size_square()

for y in range(0, size_square):
    for x in range(0, size_square):
        if dan.get_apart_list_by_cord(x, y) == 1:
            dan.search_dan(x, y)

print(dan.dangi_num -1)

sorted_dict = sorted(dan.get_dan_stat().items(), key = lambda item: item[1])
for value in sorted_dict:
    print(value[1])