# problem 2 Merge two dictionaries
# input
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


# output
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)


# def merge(dict1, dict2):
#     for key, value in dict1.items():
#         merged_dict[key] = value


# a = merge({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {
#           'Thirty': 30, 'Fourty': 40, 'Fifty': 50})
# print(a)
