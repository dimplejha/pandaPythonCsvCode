# following are 2 list of dictionary you have to megre 2 list of dictionaries using key name 
# and create a new list of dictionaries which will name , id and count or  name and count 
# based on the list_a contains 2 or one key
# # [{
#     "name":"abc",
#     "id":1,
#      "count" : 10
#   }, ...
# {
#     "name":"fasgf",
#         "count" : 23
#   },
# ....]


list_a = [
  {
    "name":"abc",
    "id":1
  },
    {
    "name":"pqr",
  },
  {
    "name":"qwe",
    "id":41
  },
  {
    "name":"rewer",
    "id":21
  },
  {
    "name":"asdgdfgh",

  },
  {
    "name":"fasgf",

  },
  {
    "name":"aghl",
    "id":211
  },
]

list_b = [
  {
    "name":"abc",
    "count" : 10
  },
    {
    "name":"pqr",
    "count" : 13
  },
  {
    "name":"qwe",
    "count" : 15
  },
  {
    "name":"rewer",
    "count" : 19
  },
  {
    "name":"asdgdfgh",
    "count" : 22
  },
  {
    "name":"fasgf",
    "count" : 23
  },
  {
    "name":"aghl",
    "count" : 24
  },
]



list_c=[]
for i in range(len(list_a)):
    temp=list_a[i] | list_b[i]
    list_c.append(temp)

print(list_c)



