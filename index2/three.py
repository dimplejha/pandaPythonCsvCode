# problem 3 rename a key city to a location in the following dictionary.
# input
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# output
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}


# d = {'a': 1, 'b': 2}
v = sample_dict['city']
del sample_dict['city']
sample_dict['location'] = v

print(sample_dict)



