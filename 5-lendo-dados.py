import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Lendo dados
data = cursor.execute("""
SELECT * FROM movies
""")
print(data.fetchall())

data = cursor.execute("""
SELECT name, year, score FROM movies
""")
print(data.fetchall())

# 4 - Interando os dados
for row in cursor.execute('SELECT * FROM movies'):
    print(f"{row}")
 
    
# 5 - Ordenando os dados pelo score
print("\nFilmes Ordenados pelo Score\n")
for row in cursor.execute('SELECT * FROM  movies ORDER BY score desc'):
    print(f'{row}')

connection.commit()

# 6 - Fechando conexão
connection.close()
