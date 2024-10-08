from flask import request
from app import app
import mysql.connector
from app.controllers.default import User 

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

def found_user(ID):
    query = "select * from users where id = %s"

    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute(query, (ID,))
        resultado = cursor.fetchone()
        if resultado:
            return User(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
        else:
            return None
    except Exception as e:
        return f'Erro ao validar usuário: {str(e)}'
    finally:
        cursor.close()
        connection.close()

def get_user_ID(user):
    query = "select id from users where username = %s"
    connection = connect_to_database()
    try:
        cursor = connection.cursor()
        cursor.execute(query, (user,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return None
    except Exception as e:
        return f'Erro ao validar usuário: {str(e)}'
    finally:
        cursor.close()
        connection.close()

# Funções de musicas 

def add_music(nome, id_criador, data_criacao, caminhoarquivo, foto_musica):
    resultado = None
    try:
        connection = connect_to_database()

        cursor = connection.cursor()
        query = 'insert into musicas (nome, id_criador, data_criacao, caminho_arquivo, foto_musica) values(%s, %s, %s, %s, %s)'
        
        cursor.execute(query, (nome, id_criador, data_criacao, caminhoarquivo, foto_musica,))

        connection.commit()

        resultado = 'Musica criada com sucesso!'

        return resultado

    except Exception as resultado:
        return str(resultado)
    finally:
        cursor.close()
        connection.close()

def verifica_musica_existente(nomeMusica):
    
    query = 'Select * from musicas where nome = %s'

    try:
        conn = connect_to_database()

        cursor = conn.cursor()
        cursor.execute(query , (nomeMusica, ))

        resultado = cursor.fetchone()

        if resultado:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return None 

def return_last_music():
    from app.controllers.config import Musica
    query = 'SELECT * FROM musicas ORDER BY id DESC LIMIT 1'
    conn = connect_to_database()
    try:
        cursor = conn.cursor()
        cursor.execute(query);
        resultado = cursor.fetchone()
        if resultado:
            print("passou")
            tmpMusica = Musica(resultado[5], resultado[4], resultado[3], resultado[2], resultado[1], resultado[0])
            return tmpMusicaw
        else:
            return None
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()
        