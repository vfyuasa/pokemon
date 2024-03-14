import sqlite3 as sql

def findPoke(code: int)->list:
    conn = sql.connect('DB\pokemon.db')
    cur = conn.cursor()
    
    cur.execute('SELECT p.name, p.type_code, t.name, t2.name FROM pokemon_main AS p LEFT OUTER JOIN mtb_type AS t ON p.type_code = t.id LEFT OUTER JOIN mtb_type AS t2 ON p.sub_type = t2.id WHERE p.id = ?', (code,))
    data = cur.fetchall()

    poke = {}
    for record in data:
        name, type_code, type_name, sub_type = record
        poke['name'] = name
        poke['type_code'] = type_code
        poke['type_name'] = type_name
        poke['sub_type'] = sub_type
            
    cur.close()
    conn.close()
    
    return poke