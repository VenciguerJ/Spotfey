from flask import request
from app import app
import mysql.connector

def connect_to_database():
    from app.controllers.config import DBConfig as db
    connection = mysql.connector.connect(
        host=db.DB_HOST,
        user=db.DB_USER,
        password=db.DB_PASSWORD,
        database=db.DB_NAME
    )
    return connection



#funções de usuário

def cadastra_user(username, senha, email, foto_perfil=None):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        if foto_perfil:
            cursor.execute("insert into users (username, senha,foto_perfil, email) values (%s, %s, %s, %s)", (username, senha, foto_perfil, email))
        else:
            cursor.execute("insert into users (username, senha, email) values (%s, %s, %s)", (username, senha, email))
    
        connection.commit()

        resultado = 'Usuário cadastrado!'

    except Exception as e:
        resultado = f'Erro no cadastro do usuário: {e}'
    finally:
        cursor.close()
        connection.close()

    return resultado

def verifica_usuario_existente(user):
    existente = None
    query = "select username from users where username = %s"
    connection = connect_to_database()

    try:
        cursor = connection.cursor()
        cursor.execute(query, (user,))
        resultados = []
        resultados = cursor.fetchall()
        if len(resultados) > 0:
            existente = True
        else:
            existente = False
    except Exception as e:
        existente = f'Erro ao validar usuário: {str(e)}'
    finally:
        cursor.close()
        connection.close()

    return existente
    

def busca_senha(user):
    query = "select senha from users where username = %s"

    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        cursor.execute(query, (user,))
        resultado = cursor.fetchall()
        if len(resultado) > 1:
            return 'mais de um usuário, erro no sistema'
        else:
            return str(resultado[0][0])
    except Exception as e:
        return f'Erro ao validar usuário: {str(e)}'
    finally:
        cursor.close()
        conn.close()
