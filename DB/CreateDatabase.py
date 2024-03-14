import sqlite3 as sql

class Databases:
    def creating(dbnm):
        sql.connect('db\\' + dbnm + '.db')
        sql.commit()
        sql.close()