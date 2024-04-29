from conexao_post import conn

cursor = conn.cursor()

games = [('Star Wars Survivor', 2023, 9.0),
         ('Luigi Mansion', 2019, 9.0)]

for game in games:
    cursor.execute("""
INSERT INTO game (name, year, score) 
VALUES (%s, %s, %s)
""", game)
    
conn.commit()
print('Dados inseridos com sucesso!')

conn.close()