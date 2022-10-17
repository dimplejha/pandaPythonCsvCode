import sqlite3
import csv


def create_database(database_name):
    con = sqlite3.connect(database_name+".db")
    print(" sqlite Database connected connected")
    con.execute('''CREATE TABLE new2
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

    with open("data.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
            for i in row:
                print(i)

    insert_records = "INSERT INTO person (NAME,AGE,ADDRESS,SALARY) VALUES(?, ?)"

    sqlite3.Cursor.executemany(insert_records, contents)

    select_all = "SELECT * FROM person"
    rows = cursor.execute(select_all).fetchall()

    for r in rows:
        print(r)

    con.commit()
    con.close()


create_database("demo")
