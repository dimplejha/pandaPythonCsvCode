import csv
import sqlite3


def read_csv():
    with open("data.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)


def database_connection():
    db_connection = sqlite3.connect('filecsv.db')
    # cursor = db_connection.cursor()
    return db_connection


def database_table():
    assign_connection = database_connection()
    table_create_cmd = '''
    CREATE TABLE CSVDATA
            (ID INT PRIMARY  KEY      NOT NULL,
            index            TEXT     NOT NULL
            company          TEXT     NOT NULL,
            length           TEXT     NOT NULL,
            numofcylinders TEXT     NOT NULL,
            averagemileage  TEXT     NOT NULL,
            price            TEXT     NOT NULL,
            location         TEXT     NOT NULL
            color            TEXT     NOT NULL);
    '''
    assign_connection.execute(table_create_cmd)
    assign_connection.close()


# def database_insertdata():
    insert_records = "INSERT INTO CSVFILE (index,company,length,num-of-cylinders,average-mileage,price,location,color) VALUES(?, ?, ?, ? ,? ,? ,? ,?)"
    cursor.executemany(insert_records, csvreader)
    select_all = "SELECT * FROM CSVFILE"
    rows = cursor.execute(select_all).fetchall()
# Output to the console screen
    for r in rows:
        print(r)
# Committing the changes
    db_connection.commit()
# closing the database connection
    db_connection.close()


database_connection()
