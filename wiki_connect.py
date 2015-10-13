# -------------------------------------------------------------------------
# Created by: Bernard Ong
# Created on: 10/11/2015
# Description: script to connect to the wiki sql database; text field test
# -------------------------------------------------------------------------

import mysql.connector
from mysql.connector import errorcode

# create a connection to the MySQL database
my_conn = mysql.connector.connect(
    user='root',
    password='J@p@n6498!',
    host='localhost',
    database='wiki')

# establish the cursor and execute the query
my_cur = my_conn.cursor()
my_query = ("select old_text from text where (instr(old_text,'Clipper')>0 and instr(old_text,'the')>0) limit 15")
my_cur.execute(my_query)
onerow = my_cur.fetchone()

while onerow is not None:
    print (onerow)
    onerow = my_cur.fetchone()

# remember to close the cursor and db connection, just to be sure
my_cur.close()
my_conn.close()

# -------------------------------------------------------------------------
# code end
# -------------------------------------------------------------------------
