## importing 'pymysql' module to create connection with remote database
import pymysql

## passing credential for our database

conn = pymysql.connect(
    host='sql12.freesqldatabase.com',
    database='sql12717114',
    user='sql12717114',
    password='ugrUHPjwx2',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Cursor Object: used to execute SQL statements on the sqlite database

cursor = conn.cursor()

# defining SQL Query to create or table 

sql_query = """    DROP TABLE book; """

# Now we need to execute this query 

cursor.execute(sql_query)

sql_query = """    CREATE TABLE book (

        id integer PRIMARY KEY AUTO_INCREMENT, 
        author text NOT NULL,
        language text NOT NULL,
        title text NOT NULL

);"""
# Now we need to execute this query 

cursor.execute(sql_query)

conn.close() # to close the database connection