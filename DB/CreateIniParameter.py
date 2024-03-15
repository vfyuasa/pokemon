import sqlite3 as sql

conn = sql.connect('DB\pokemon.db')
cur = conn.cursor()

cur.execute('CREATE TABLE mtb_pokemon_ini_parameter(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, main_code INTEGER, attack INTEGER, special_attack INTEGER, defence INTEGER, special_difence INTEGER, speed INTEGER)')

conn.commit()

cur.close()
conn.close()