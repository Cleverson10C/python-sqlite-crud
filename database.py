import sqlite3

def conectar():
    return sqlite3.connect('pessoas.db')


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            classificacao TEXT NOT NULL 
        )       
    ''')

    conn.commit()
    conn.close()