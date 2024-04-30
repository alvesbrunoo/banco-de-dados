from conexao_post  import conn

cursor = conn.cursor()

sql = """UPDATE game 
    SET name = %s
    WHERE id = %s"""


cursor.execute(sql, ("Fifa 23", 6))

sql = """UPDATE game
    SET score = %s
    WHERE id = %s"""

cursor.execute(sql, (8.5, 6))

conn.commit()
print('Dados atualizados com sucesso!')

conn.close()