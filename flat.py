

numbers = [[1, [12, 34, 56], 2, 3], [4, 5, [98, 76, 54], 6]]


def rec(list_num):
    for i in list_num:
        if type(i) == list:
            rec(i)
        else:
            print(i)


rec(numbers)
