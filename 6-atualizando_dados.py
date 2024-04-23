import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Solicitando dados do usuário
id = int(input('Informe o id do filme que deseja atualizar\n'))
name = input('Informe o novo nome do filme\n')
score = float(input('Informe a nova nota\n'))

# 4 - Atualizando dados
cursor.execute("""
UPDATE movies set name = ?
WHERE id = ?
""", (name, id))


cursor.execute("""
UPDATE movies set score = ?
WHERE id = ?
""", (score, id))

connection.commit()
print('Dados atualizados com sucesso!')

# 5 - Fechando conexão
connection.close()