# coding: utf-8


# list1 = [1, 45, 32, 65, 78, 22, 98, 101, 12]
#
#
# def test(list1):
#     length1 = len(list1)
#     for i in range(length1):
#         for j in range(0, length1 - i - 1):
#             if list1[j] > list1[j + 1]:
#                 list1[j], list1[j + 1] = list1[j + 1], list1[j]
#     return list1
#
#
# def test1(list1):
#     length = len(list1)
#     while True:
#         flag = False
#         for i in range(length-1):
#             if list1[i] > list1[i+1]:
#                 list1[i], list1[i + 1] = list1[i + 1], list1[i]
#                 flag = False
#         if not flag:
#             break
#     return list1
#
#
# a = 20
#
#
# def func():
#     global a
#     a = 30
#     return a
# # func()
# # print(a)
#
#
# def div1(x, y):
#     print("%s/%s = %s" % (x, y, x/y))
#
#
# def div2(x, y):
#     print("%s//%s = %s" % (x, y, x // y))

#
# div1(5, 2)
#
# div1(5., 2)
#
# div2(5, 2)
#
# div2(5., 2.)


# list2 = [1, 2, 3, [4, 5, 6], {"a": 5}]
# import copy
#
# b = copy.copy(list2)
# c = copy.deepcopy(list2)
# print("=======================")
# print(list2, id(list2))
# print([id(i) for i in list2])
# print("=======================")
# print(b, id(b))
# print([id(i) for i in b])
# print("=======================")
# print(c, id(c))
# print([id(i) for i in c])
# print("=======================")
#
#
# list2[-2].pop(1)
# list2[-1]["a"] = 11
# print(list2)
# print(b)
# print(c)
import random


# t = ""
# for i in range(16):
#     t += str(random.randrange(0, 9))
# print(t)


# import random
# checkcode = ''
# num = []
# for i in range(4):
#     tep1 = chr(random.randint(65, 97))
#     tep2 = random.randint(0, 9)
#     num.append(tep1)
#     num.append(tep2)
#
# for i in range(4):
#     checkcode += str(random.choice(num))
#
# print(checkcode)

# import re
# p1 = "123<.qewqe>dad<dsadasd>aadas><>>>>1231><11"
# print(re.findall("<.*>", p1))
# print(re.findall("<.*?>", p1))

