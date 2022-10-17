import csv
import sqlite3

# Connecting to the geeks database

connection = sqlite3.connect('g4g.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE new10
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);
                '''
connection.execute("INSERT INTO new2 (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")
# Creating the table into our
# database
cursor.execute(create_table)
print(create_table)

# Opening the person-records.csv file
file = open('data.csv')

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)

# SQL query to insert data into the
# person table
insert_records = "INSERT INTO person (NAME,AGE,ADDRESS,SALARY) VALUES(?, ?,?,?)"

# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the person table To verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM person"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()

# closing the database connection
connection.close()
