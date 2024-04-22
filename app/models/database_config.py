import mysql.connector

class config:
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = '1234'
    DB_NAME = 'spotfei'
    DB_PORT = '3306'

def connect_to_database():
    connection = mysql.connector.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    return connection

def cadastra_user(username, senha, email, foto_perfil=None):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        if foto_perfil:
            cursor.execute(f"insert into users (username, senha, foto_perfil, email) values ('{username}', '{senha}', '{foto_perfil}', '{email}')")
        else:
            cursor.execute(f"insert into users (username, senha, email) values ('{username}', '{senha}', '{email}')")
    
        connection.commit()
     
        resultado = 'Usuário cadastrado!'
      
        
    except Exception as ex:
        resultado = f'Erro no cadastro do usuário: {ex}'
    finally:
        cursor.close()
        connection.close()

    return resultado
