from conexao_post import conn

cursor = conn.cursor()

result = cursor.execute("""SELECT * FROM game""")

# result = cursor.fetchall()

print(cursor.fetchall())
