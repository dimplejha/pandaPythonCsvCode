#  In the following list of dictionary in some of the dictionary id key is not present
# if id key is not present then add id as key with default value of 0 "zero"

from re import A


list_a = [
    {
        "name": "abc",
        "id": 1
    },
    {
        "name": "pqr",
    },
    {
        "name": "qwe",
        "id": 41
    },
    {
        "name": "rewer",
        "id": 21
    },
    {
        "name": "asdgdfgh",

    },
    {
        "name": "fasgf",

    },
    {
        "name": "aghl",
        "id": 211
    },
]


# for x in list_a:
#     if 'id' not in x:
#         x['id'] = 0
# print(list_a)


compression = [x.setdefault(0) for x in list_a if 'id' not in x]

print(compression)


txt = "Hello World" [0:6:2]
print(txt)


a = [1, 2, 3, 4, 5][0:5:5]
print(a)


def swap(list):

    start = list.pop(0)
    end = list.pop(-1)

    list.insert(0, end)
    list.append(start)

    return list


# Driver code
a = [1, 2, 3, 4, 5]

print(swap(a))


# def swapList(list):

#     start = list[-1], list[0]

#     list[0], list[-1] = start

#     return list


# newList = [1, 2, 3, 4, 5]
# print(swapList(newList))


# swap 1st and last value in list
z = [1, 2, 3, 4, 5]
a=[]
