import sqlite3

# Código para criar a tabela no banco de dados SQLite3
conn = sqlite3.connect("meu_banco_de_dados.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS dados_monitoramento (
        id INTEGER PRIMARY KEY,
        cpu_percent FLOAT,
        memory_percent FLOAT,
        disk_percent FLOAT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""
)

conn.commit()
conn.close()
