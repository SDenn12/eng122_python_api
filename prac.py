import math


# from itertools import permutations
# def permutations_(s):
#     return ([''.join(p) for p in permutations(s)])
#
#
# print(len(permutations_("aabb")))

import math


# def permutations_(s):
#     iteration = []
#     letters = [c for c in s]
#     location = 0
#     while len(iteration) < 24:
#         letters[location], letters[location % (len(letters) - 1)] = letters[location % (len(letters) - 1)], letters[location]
#         iteration.append(letters)
#         location = location % (len(letters) - 1)
#
#     return iteration
#
# print(permutations_("aabb"))

import math
def zeros(n):
    num = n
    two_count = 0
    five_count = 0
    counter = True
    while counter:
        if num % 5 == 0:
            num = n/5
            five_count += 1
        else:
            counter = False
    print(two_count)
    print(five_count)
    if two_count % 2 == 0 and five_count % 2 == 0:
        return two_count
    elif two_count % 2 == 1 and five_count % 2 == 1:
        return five_count
    else:
        return 0




print(zeros(6))