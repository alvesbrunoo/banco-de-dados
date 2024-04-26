import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Solicitando dados do usuário
name = input('Qual o nome do Filme\n')
year = int(input('Qual o ano do Filme\n'))
score = float(input('Nota do Filme\n'))

cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES (?, ?, ?)
""", (name, year, score))

# 4 - Inserindo Dados
cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Super Mario Bros', 2023, 9.5 )
""")
        
cursor.execute("""
INSERT INTO movies (name, year, score)
VALUES ('Avatar', 2023, 10.0)
""")     

cursor.execute("""
INSERT INTO movies (name, year, score)   
VALUES ('Velozes e Furiosos', 2023, 8.5)     
""")               

# 5 - Gravando Dados no BD
connection.commit()
print('Dados inseridos com sucesso!')

# 6 - Fechando conexão
connection.close()