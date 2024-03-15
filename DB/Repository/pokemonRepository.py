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

    if data:
        cur.execute('SELECT attack, special_attack, defence, special_difence, speed FROM mtb_pokemon_ini_parameter WHERE main_code = ?', (code,))
        parameter = cur.fetchall()
        
        para = {}
        for record in parameter:
            attack, special_attack, defence, special_defence, speed = record
            para['attack'] = attack
            para['special_attack'] = special_attack
            para['defence'] = defence
            para['special_defence'] = special_defence
            para['speed'] = speed
        
        poke['parameter'] = para

    cur.close()
    conn.close()
    
    return poke