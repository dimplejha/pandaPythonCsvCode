import csv
import sqlite3


con = sqlite3.connect('database.db')
print("created database")
# val = input("enter table  name:=")

# Table Definition


def table_create(table_name):
    create_table = f'''CREATE TABLE {table_name}(
                
               
                NAME TEXT NOT NULL,
                AGE INTEGER NOT NULL,
                ADDRESS TEXT NOT NULL,
                SALARY TEXT NOT NULL);
                '''
    con.execute(create_table)
    print(create_table)


file = open('data.csv')
contents = csv.reader(file)


def insert_data(data):

    for i in contents:
        con.execute(f'''INSERT INTO gfur (NAME,AGE,ADDRESS,SALARY) \
        VALUES ("{i[0]}", "{i[1]}", "{i[2]}", "{i[3]}" )''')
        con.commit()


# closing the database connection
# con.close()
# table_create("dimple4")

insert_data("data")
