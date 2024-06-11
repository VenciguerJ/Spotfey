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
    from app.controllers.utils import valida_arquivo, verifica_arquivo_dupicado, ConstUsers

    CaminhoArquivo = None

    #registro
    if request.method == 'POST':
        user = request.form['form_user']
        email = request.form['form_email']
        password = request.form['form_password']
        fotoPerfil = request.files['form_profile_picture']
        password2 = request.form['form_password2']


        #validação de user
        if verifica_arquivo_dupicado(user) == True:
            user = None
            #colocar aviso de user já cadastrado
        else:
            if str(user).lenght > ConstUsers.MAX_CARACTERES_USERNAME:
                user = None
                #aviso de usuário com nome muito grande

        
        #validação de email

        if str(email).lenght > ConstUsers.MAX_CARACTERES_EMAIL:
            email = None


        #validação de senha
        definitivePassword = None
        if password == password2:
            definitivePassword = password
            if definitivePassword.lenght > ConstUsers.MAX_CARACTERES_SENHA:
                definitivePassword = None
                #mensagem de usuário muito grande
        else:
            definitivePassword = None
            #mensagem de erro não condizem e barrar        

        # validação do arquivo
        if fotoPerfil:
            nomeArquivo = secure_filename('profile' + os.path.splitext(fotoPerfil.filename)[1])

            if valida_arquivo(nomeArquivo):

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
                #mensagem de extensões não suportadas


        if user != None and definitivePassword != None and email != None:
            msg = cadastra_user(user, password, email, CaminhoArquivo)
            msg = str(msg)
            return render_template('login_success.html', caminho=CaminhoArquivo, msg=msg)
        else:
            msg = ''
            #fazer um aviso na própria poágina das informações que faltam'
    #elif request.method == 



    caminho = f"foto de perfil é a {nomeArquivo}"

    


