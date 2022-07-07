# set1 = {1, 2, 3, 4, 5, }
# set2 = {1, 2, 3, 4, 5, 6, 4, }
# set1.update(set2)
# print(set1)
# print(set1.union(set2))

# set1 = {1, 2}
# set2 = {3}
# set3 = {4, 5}
# set4 = {3, 2, 6}
# set5 = {6}
# set6 = {7, 8}
# set7 = {9, 8}
# set4.intersection_update(set5)
# new = set5.union(set4)
# print(new)
# set1.union(set2, set3, set4, set5, set6, set7)
# print(set1)

# def compare(set1: set, set2: set):
#     if set1 == set2:
#         print("Sets are equal")
#     elif set1 < set2:
#         print("set2 is a superset for set1")
#     elif set1 > set2:
#         print("set1 is a superset for set2")
#     else:
#         print("Superset is not detected")
# compare({1, 2, 3, },
#         {1, 2, 4, })
#
# def elephant_beats_check(x1, x2, y1, y2):
#     if abs(x1 - y1) == abs(x2 - y2):
#         return "Да"
#     else:
#         return "Нет"
# print(elephant_beats_check(4, 4, 6, 5))

# import datetime
# lists = []
# time_now = datetime.datetime.now()
# for i in range(1, 1001):
#     lists.append(i)
# delta = datetime.datetime.now() - time_now
# print(delta)
#
# time_now1 = datetime.datetime.now()
# new_list = [i for i in range(1, 1001)]
# delta1 = datetime.datetime.now() - time_now1
# print(delta1)
# print(delta / delta1, "times faster")
#
# spam = [i**2 for i in range(1, 1001)]
# print(spam)
# print(max(2, 4, 5, ))

# n = int(input("n: "))
# c = 1
# for i in range(1, n+1):
#     c = c * i
# print(c)

# my_list = ["word", "hello", "python"]
# generated_dict  = {k: k+k for k in my_list}
# print(generated_dict)

import random
lists = ["scissors", "rock", "paper"]
pc_score = 0
user_score = 0
user_name = input("Your name, please: ")
while True:
    pc_choice = random.choice(lists)
    user_choice = input("Your turn: ").lower()
    if pc_choice == user_choice:
        print(f"Computer: {pc_choice}")
        print("It's a tie!")
    elif pc_choice == lists[0] and user_choice == lists[1] \
            or pc_choice == lists[1] and user_choice == lists[2]\
            or pc_choice == lists[2] and user_choice == lists[0]:
        user_score += 1
        print(f"Computer: {pc_choice}\n"
              f"{user_name} won!\n"
              f"Computer: {pc_score}\n{user_name}: {user_score}")
    else:
        pc_score += 1
        print(f"Computer: {pc_choice}\n"
              "Computer won!\n"
              f"Computer: {pc_score}\n{user_name}: {user_score}")
    if user_score == 2 or pc_score == 2:
        break










