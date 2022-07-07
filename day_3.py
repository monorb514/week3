# functions
import random
# def move(lists):
#     for i in lists:
#         x = random.randint(0, 2)
#         if i[x] == 0:
#             i[x] = "X"
#         else:
#            continue
#     return lists
# print(move([[0, 0, "O"],
#      [0, "O", "X"],
#      [0, "X", 0]]))


def is_winner(lists):
    d1 = 0
    d2 = 0
    for i in range(3):
        temp = lists[i][0]
        temp1 = lists[0][i]
        row = 0
        col = 0
        for j in range(3):
            if lists[i][j] == temp:
                row += 1
            if lists[j][i] == temp1:
                col += 1
        if row == 3 or col == 3:
            return True
        else:
            for i in range(3):
                if lists[i][i] == lists[0][0]:
                        d1 += 1
                if lists[i][2-i] == lists[0][2]:
                        d2 += 1
            if d1 == 3 or d2 == 3:
                return True
            else:
                return False


print(is_winner([["O", "O", "X"],
                 ["O", "X", "O"],
                 [0, "O", "X"]]))

# def is_winner(lists):
#     visited = []
#     current = lists[0][0]


def example(**kwargs):
    for k, v in kwargs.items():
        if type(v) == str:
            kwargs[k] = v.title()
        if type(v) == set:
            kwargs[k] = list(v)
    return kwargs
print(example(name = "nazgul", age = 50, sets = {2, 4, 5, 7, 8}))














