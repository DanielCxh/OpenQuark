#!/usr/bin/python3

# couldn`t name the file as sqlite3,
# because this name is a internal name.

# import sqlite3 library
import sqlite3 as sql

###############################################################################
# SQL commands
###############################################################################
SQL_CMD_CREATE_TBL = ''
SQL_CMD_SELECT     = ''

###############################################################################
# sqlite3.connect(database [,timeout ,other optional arguments])
###############################################################################
# Connect to a exist DB test.db,
# if the DB is not exist will create it.
conn = sql.connect('test.db')

###############################################################################
# connection.cursor([cursorClass])
###############################################################################
c = conn.cursor()

###############################################################################
# cursor.execute(sql [, optional parameters])
###############################################################################
c.execute('''CREATE TABLE STOCK
	    (ID INT PRIMARY KEY NOT NULL,
	     CODE TEXT NOT NULL,
	     NAME TEXT NOT NULL);''')

###############################################################################
# connection.commit()
###############################################################################
conn.commit()

###############################################################################
# connection.close()
###############################################################################
conn.close()

