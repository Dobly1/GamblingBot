import sqlite3
from sqlite3 import Error

'''
conn = sqlite3.connect('player_info2.db')
c = conn.cursor()

def createTable(c):
    c.execute('CREATE TABLE IF NOT EXISTS player_data (discord_id INTEGER PRIMARY KEY, credits INTEGER)')

def addData(c):
    #.execute('INSERT INTO player_data (discord_id, credits) VALUES(1237, 11)')

def getData(c):
    c.execute('SELECT * FROM player_data WHERE discord_id=1236')
    rows = c.fetchall()
    for row in rows:
        print (row)

createTable(c)
addData(c)
getData(c)

conn.commit()
conn.close()
'''

class DBconnect:
    def create_connection(db_name):
        conn = None
        try:
            conn = sqlite3.connect(db_name)
            return conn
        except Error as e:
            print(e)
        return conn

    def create_table(conn):
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS player_data (discord_id INTEGER PRIMARY KEY, credits INTEGER)')

    def insert_data(conn,user_id,balance):
        print("Attempting to add "+str(user_id)+" with a balance of "+str(balance))
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO player_data (discord_id, credits) VALUES(?, ?)',[user_id,balance])
            conn.commit()
        except Error as e:
            print(e)

    def find_data(conn,user_id):
        cur = conn.cursor()
        try:
            cur.execute('SELECT * FROM player_data WHERE discord_id=?',[user_id])
            return cur.fetchall()[0]
        except Error as e:
            print(e)

