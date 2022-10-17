import csv
import sqlite3

# con = sqlite3.connect('database.db')
print("created database")

file = open('data.csv')
contents = csv.reader(file)
for i in contents:

    final = (f"INSERT INTO lkjhgf (NAME,AGE,ADDRESS,SALARY) \
      VALUES ({i[0]}, {i[1]}, {i[0]}, {i[0]} )")
    print(type(final))
