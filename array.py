

# numbers = [[1, [12, 34, 56], 2, 3], [4, 5, [98, 76, 54], 6]]
# # for x in numbers:
# #     for y in x:
# #         print(y)

# a_list = []
# for a in numbers:
#     if type(a) is list:
#         print(type(a))
#     a_list.append(a)
#     print(a_list, "=============================================")
#         for b in a:
#             if type(b) is list:
#                 print(type(b))
#             a_list.append(b)
#             print(a_list)


# #     print(a_list)
# # print(a_list)


#numbers = [[1, [12, 34, 56], 2, 3], [4, 5, [98, 76, 54], 6]]
# a_list = []
# for x in numbers:
#     for y in x:
#         if type(y) is list:
#             # print(y, "==========")
#             print(type(y))
#             for z in y:
#                 if type(z) is list:
#                 # print(z)
#                 a_list.append(z)
#         else:
#             a_list(y)

# print(a_list)


numbers = [[1, [12, 34, 56], 2, 3], [4, 5, [98, 76, 54], 6]]
listdata = []
for x in numbers:
    for y in x:
        if type(y) is list:
            for z in y:
                # print(type(z))
                if type(z) is list:
                    for a in z:
                        # print(type(a))
                        listdata.append(a)
                else:
                    listdata.append(z)
        else:
            listdata.append(y)
print(listdata)


def factorial(n):
    if n == 1:
        return n
    else:
        # return n*factorial(n-1)
        for x in numbers:
            for y in x:
            


print(factorial([[1, [12, 34, 56], 2, 3], [4, 5, [98, 76, 54], 6]]))








