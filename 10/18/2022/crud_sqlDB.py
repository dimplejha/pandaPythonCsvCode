import csv
import sqlite3


def connection_established():
    con = sqlite3.connect("final.db")
    print("database connected")
    return con


def create_table(table_name):
    try:
        con = connection_established()
        con_a = con.cursor()
        table = f""" CREATE TABLE {table_name} (
            Name TEXT  NULL,
            AGE TEXT  NULL,
            ADDRESS TEXT,
            SALARY TEXT
        ); """

        print(type(table))
        con_a.execute(table)
        print("table is created")
        return {table_name}
    except sqlite3.Error as error:
        print("Fail to create table in sqlite", error)


file = open("data.csv")
contents = csv.reader(file)
print(contents)


def batch_insert_data():

    con = connection_established()

    # for i in contents:
    # insert_records = f'INSERT INTO kkuq12 (NAME,AGE,ADDRESS,SALARY) VALUES("{i[0]}","{i[1]}","{i[2]}","{i[3]}")'
    insert_records = f'INSERT INTO rohan (NAME,AGE,ADDRESS,SALARY) VALUES(?,?,?,?)'
    con.executemany(insert_records, contents)
    print(insert_records, contents)
    print(insert_records)
    con.commit()

# def inser():


# connection_established()
# create_table("rohan")
batch_insert_data()
