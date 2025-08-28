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

def load_players():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT name, balance, position, in_jail FROM players")
    rows = c.fetchall()
    conn.close()
    return [{"name": r[0], "balance": r[1], "position": r[2], "in_jail": r[3]} for r in rows]

def save_players(players):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM players")
    for p in players:
        c.execute("INSERT INTO players VALUES (?, ?, ?, ?)",
                  (p["name"], p["balance"], p["position"], p["in_jail"]))
    conn.commit()
    conn.close()

def load_ownership():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT property, owner FROM ownership")
    rows = c.fetchall()
    conn.close()
    return {r[0]: r[1] for r in rows}

def save_ownership(ownership):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM ownership")
    for prop, owner in ownership.items():
        c.execute("INSERT INTO ownership VALUES (?, ?)", (prop, owner))
    conn.commit()
    conn.close()