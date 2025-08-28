# player_manager.py
# Handles player setup and saving/loading

import sqlite3

DB = "monopoly.db"

def setup_database():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS players
                 (name TEXT PRIMARY KEY, balance INTEGER, position INTEGER, in_jail INTEGER)""")
    c.execute("""CREATE TABLE IF NOT EXISTS ownership
                 (property TEXT PRIMARY KEY, owner TEXT)""")
    conn.commit()
    conn.close()