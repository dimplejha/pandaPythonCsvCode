import sqlite3





def datbase_connection(database_name):

    con = sqlite3.connect(database_name+".db")
    print(" sqlite Database connected connected")
    return con


def create_table():
    con = datbase_connection("database_name")

    con.execute('''CREATE TABLE d
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

    con.execute("INSERT INTO d (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    con.commit()


# con.close()


datbase_connection("demo")
create_table()
