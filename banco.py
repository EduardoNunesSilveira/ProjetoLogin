import sqlite3

DATABASE = "banco.db"


def conectar():
    conn = sqlite3.connect(DATABASE)
    return conn


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            usuario TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def cadastrar_usuario(nome,usuario,senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios(nome,usuarios,senha)
        VALUES (?, ?, ?)
    """, (nome,usuario,senha))

conn.commit()
conn.close()


def verificar_usuario(usuario, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM usuarios
        WHERE usuarios = ? AND senha = ?
    """, (usuario, senha))

    resultado = cursor.fetchone()

    conn.close()
    return resultado
    

