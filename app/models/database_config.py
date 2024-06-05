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


#Funções gerais

def valida_arquivo(filename):
    from app.config import Config
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

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
