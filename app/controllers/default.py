from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import app, config
import os

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/success', methods=['GET', 'POST'])
def successful_login():
    from app.models.database_config import cadastra_user
    from app.controllers.utils import valida_arquivo, verifica_arquivo_dupicado

    CaminhoArquivo = None

    if request.method == 'POST':
        user = request.form['form_user']
        email = request.form['form_email']
        password = request.form['form_password']
        fotoPerfil = request.files['form_profile_picture']

        nomeArquivo = secure_filename('profile' + os.path.splitext(fotoPerfil.filename)[1])

        if valida_arquivo(nomeArquivo):

            if fotoPerfil == None:
                msg = 'deu merda aqui'
            else:

                CaminhoArquivo = os.path.join(config.Config.UPLOAD_IMAGES, user)
                print(os.path.join(CaminhoArquivo, nomeArquivo))

                verifica_arquivo_dupicado(nomeArquivo, CaminhoArquivo)

                if not os.path.exists(CaminhoArquivo):
                    os.makedirs(CaminhoArquivo)
                    fotoPerfil.save(os.path.join(CaminhoArquivo, nomeArquivo))
                else:
                    fotoPerfil.save(os.path.join(CaminhoArquivo, nomeArquivo))
        else:
            msg = 'erro :('
    #elif request.method == 



    caminho = f"foto de perfil é a {nomeArquivo}"

    msg = cadastra_user(user, password, email, CaminhoArquivo)
    msg = str(msg)
    caminho  = str(CaminhoArquivo)
    return render_template('login_success.html', caminho=CaminhoArquivo, msg=msg)


