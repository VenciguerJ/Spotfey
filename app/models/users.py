import mysql.connector


# Estabelecer conexão com o servidor MySQL
def Conecta_DB():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="spotfeys"
    )
    return conexao


def Cria_user(nome, user, senha, foto):
    conexao = Conecta_DB()

    db = conexao.cursor()

    db.execute(f'insert into users values(default, "{nome}", "{user}", "{senha}", {foto})')

    resultados = db.fetchall()
    db.close()
    conexao.close()




