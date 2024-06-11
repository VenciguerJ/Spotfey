from flask import request
from app import app
import mysql.connector

def connect_to_database():
    from app.config import DBConfig as db
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
    query = f"select username from user where username = '{user}'"
    connection = connect_to_database()

    try:
        cursor = connection.cursor
        cursor.execute(query)
        resultados = cursor.fetchall()
        for user in resultados:
            if user:
                existente = True
            else: existente = False
        return existente
    except Exception:
        existente = f'Erro ao validar usuário: {Exception}'
        return existente
