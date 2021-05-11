from mysql.connector import connect, Error


locadora = {
    "host": "localhost", "user": "root",
    "password": "root", "database": "locadora"}

def execute(sql, params=None): # Executa um comando no mysql e salva os valores. Serve para:
    # insert, update, delete, create, alter, drop
    with connect(**locadora) as conn:  #conecta ao banco
        with conn.cursor() as cursor: # abre a página para execução
            cursor.execute(sql, params)  # executa o sql que está sendo passado
            conn.commit() # grava no banco de dados
            return cursor.lastrowid


def query(sql, params=None):
    with connect(**locadora) as trabalho:
        with trabalho.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

def insert(tabela, colunas, valores):
    return execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for valor in valores])})", valores)

def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))

def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])


def select_like(tabela, chave, valor_chave):
    return query(f"""SELECT * FROM {tabela} WHERE {chave} LIKE %s""", (valor_chave))

def select(tabela, chave, valor_chave=1, limit=100, offset=0):
    return query(f"""SELECT * FROM {tabela} WHERE {chave} LIKE %s LIMIT {limit} offset {offset}""", (valor_chave,))




# tirar dúvidas neste arquivo