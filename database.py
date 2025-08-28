import sqlite3

DB = "monopoly.db"

def connect():
    
    return sqlite3.connect(DB)

def setup_database():
    conn = connect()
    c = conn.cursor()
    # players table
    c.execute("""CREATE TABLE IF NOT EXISTS players
                 (name TEXT PRIMARY KEY, balance INTEGER, position INTEGER, in_jail INTEGER)""")
    # ownership table
    c.execute("""CREATE TABLE IF NOT EXISTS ownership
                 (property TEXT PRIMARY KEY, owner TEXT)""")
    conn.commit()
    conn.close()