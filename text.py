# import numpy as np
#
#
# def bubble_sort(lists):
#     count = len(lists)
#     for i in range(0, count):
#         for j in range(i + 1, count):
#             if lists[i] > lists[j]:
#                 lists[i], lists[j] = lists[j], lists[i]
#         return lists
#
# html = "https://www.baidu.com/s"
#
# html = html.split("?")
# print(html)

# import os
#
# print(os.listdir())
#
# my_list=[lambda:i for i in range(5)]
# print(my_list)
# for l in my_list:print(l())

arr=[19,29,30,48]

x = arr[0]

for i in arr:
    if x < i:
        x = i

print(x)
