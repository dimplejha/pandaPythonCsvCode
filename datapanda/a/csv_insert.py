
# Import required modules
import csv
import sqlite3
from string import ascii_lowercase


def db_connection():
    pass


def create_table(table_name):

    connection = sqlite3.connect('infotest.db')
    create_table = '''CREATE TABLE person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL);
                    '''

    connection.execute(create_table)
    connection.commit()
    connection.close()


def batch_insert(file_name):
    connection = sqlite3.connect('infotest.db')
    cursor = connection.cursor()
    file = open(file_name)
    contents = csv.reader(file)
    for i in contents:
        insert_query = f'INSERT INTO person (name, age) VALUES("{i[0]}","{i[1]}" )'
        connection.execute(insert_query)
    connection.commit()
    connection.close()


# def deleteRecord():
    try:
        connection = sqlite3.connect('infotest.db')
        cursor = connection.cursor()
        print("Connected to SQLite")

        # Deleting single record now
        sql_delete_query = """DELETE from person where id = 6"""
        cursor.execute(sql_delete_query)
        connection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("the sqlite connection is closed")


# def updateSqliteTable(id, salary):
    try:
        connection = sqlite3.connect('infotest.db')
        cursor = connection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update person set age = ? where id = ?"""
        data = ("age", id)
        cursor.execute(sql_update_query, data)
        connection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("The sqlite connection is closed")


def updateMultipleColumns(id, name, age):
    try:
        connection = sqlite3.connect('infotest.db')
        cursor = connection.cursor()
        print("Connected to SQLite")

        sqlite_update_query = """Update person set name = ?, age = ? where id = ?"""
        columnValues = (name, age, id)
        cursor.execute(sqlite_update_query, columnValues)
        connection.commit()
        print("Multiple columns updated successfully")
        connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update multiple columns of sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("sqlite connection is closed")


def deleteMultipleRecords(idList):
    try:
        connection = sqlite3.connect('infotest.db')
        cursor = connection.cursor()
        print("Connected to SQLite")
        sqlite_update_query = """DELETE from person where id = ?"""

        cursor.executemany(sqlite_update_query, idList)
        connection.commit()
        print("Total", cursor.rowcount, "Records deleted successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete multiple records from sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("sqlite connection is closed")


idsToDelete = [(8,), (14,)]
deleteMultipleRecords(idsToDelete)

# updateMultipleColumns(3, "hrshita", 88)
# batch_insert('records1.csv')



 


