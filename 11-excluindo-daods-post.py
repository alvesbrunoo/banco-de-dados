from conexao_post import conn

cursor = conn.cursor()

sql = """DELETE FROM game
    WHERE id = %s"""
    
cursor.execute(sql, (6, ))

sql = """DELETE FROM game
    WHERE id = %s"""
    
cursor.execute(sql, (7,))

conn.commit()
print('Dados removidos com sucesso!')

conn.close()