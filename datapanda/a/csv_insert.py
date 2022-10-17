
# Import required modules
import csv
import sqlite3


def db_connection():
    pass


def create_table(table_name):
    # Connecting to the geeks database
    connection = sqlite3.connect('infotest.db')

    # Creating a cursor object to execute
    # SQL queries on a database table

    # Table Definition
    create_table = '''CREATE TABLE person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL);
                    '''

    # Creating the table into our
    # database
    connection.execute(create_table)
    # Committing the changes
    connection.commit()

    # closing the database connection
    connection.close()


def batch_insert(file_name):
    # Opening the person-records.csv file
    connection = sqlite3.connect('infotest.db')
    cursor = connection.cursor()
    file = open(file_name)

    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)
    for i in contents:
        insert_query = f'INSERT INTO person (name, age) VALUES("{i[0]}","{i[1]}" )'
        connection.execute(insert_query)
    # SQL query to insert data into the
    # person table
    # insert_records = "INSERT INTO person (name, age) VALUES(?, ?)"

    # # Importing the contents of the file
    # # into our person table
    # cursor.executemany(insert_records, contents)

    # Committing the changes
    connection.commit()

    # closing the database connection
    connection.close()


batch_insert('records.csv')
