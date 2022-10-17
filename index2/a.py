fruits = ('apple', )
print(fruits, type(fruits))

# asscessing data from list of dict

person = [
    {
        "name": "dimple",
    },
    {
        "surname": "Jha"
    },
    {
        "number": 12
    }
]
# a = person[0].values()
# print("My name is", a)

# b = person["number"]
# print(b)


# c = person.get("name")
# print(c)

for i in person:
    d = i["name"]
    print(d)
    break


print(person[0]["name"])







    


