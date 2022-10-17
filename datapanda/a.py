gfg = "geeksforgeeks"
print(gfg[::-1])


for i in gfg:
    if 's' in i:
        print(i)


List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# accessing an element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[3])


q = ('a', 'b', 'c')
print(type(q))
# z = list(q)
z[1] = 'z'
q = tuple(z)
q = tuple(z)[1]
print(q)
