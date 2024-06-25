from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app import app
import os

from app.controllers import config

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST']) #contém os formulários de login e registro e redireciona o registro para a mesma pagina para logar
def register():
    from app.models.database_config import cadastra_user, verifica_usuario_existente
    from app.controllers.utils import valida_arquivo, verifica_arquivo_dupicado, ConstUsers
    from app.controllers.config import Config as config



    if request.method == 'POST':
        user = request.form['form_user']
        email = request.form['form_email']
        password = request.form['form_password']
        fotoPerfil = request.files['form_profile_picture']
        password2 = request.form['form_password2']

        # Validação de usuário
        if verifica_usuario_existente(user):
            flash('Usuário já cadastrado')
            return redirect(url_for('register'))
        elif len(user) > ConstUsers.MAX_CARACTERES_USERNAME:
            flash('Nome de usuário muito grande')
            return redirect(url_for('register'))

        # Validação de email
        if len(email) > ConstUsers.MAX_CARACTERES_EMAIL:
            flash('Email muito grande')
            return redirect(url_for('register'))

        # Validação de senha
        if password != password2:
            flash('Senhas não coincidem')
            return redirect(url_for('register'))
        elif len(password) > ConstUsers.MAX_CARACTERES_SENHA:
            flash('Senha muito grande')
            return redirect(url_for('register'))
        else:
            definitivePassword = password

        # Validação do arquivo
        caminhoArquivo = None
        if fotoPerfil:
            nomeArquivo = secure_filename('profile' + os.path.splitext(fotoPerfil.filename)[1])
            if valida_arquivo(nomeArquivo):
                caminhoArquivo = os.path.join(config.UPLOAD_IMAGES, user)
                if not os.path.exists(caminhoArquivo):
                    os.makedirs(caminhoArquivo)

                if verifica_arquivo_dupicado(nomeArquivo, caminhoArquivo):
                    flash('Não foi possível salvar arquivo')
                    return redirect(url_for('register'))
                else:
                    fotoPerfil.save(os.path.join(caminhoArquivo, nomeArquivo))
                    caminhoArquivo = os.path.join(caminhoArquivo, nomeArquivo)
                    profiledir = f'uploads/images/{user}/{nomeArquivo}'
            else:
                flash('Extensão de arquivo não suportada')
                return redirect(url_for('register'))
        else:
            caminhoArquivo = str(config.DEFAULT_PROFILE_IMAGE).replace(r'\\', r"/")
            profiledir = config.HTML_SOURCE_IMAGE

        # Se todas as validações passarem
        msg = cadastra_user(user, definitivePassword, email, caminhoArquivo)
        msg = str(msg)
        print(caminhoArquivo)
        return render_template('login_success.html', msg=msg, profiledir=profiledir, nome=user)
    
    return render_template('login.html')
      
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        from app.models.database_config import busca_senha, verifica_usuario_existente

        loginUser = request.form['user-form-login']
        loginPassword = request.form['password-form-login']
        
        if verifica_usuario_existente(loginUser):
            senhaDoBanco = busca_senha(loginUser)
            senhaDoBanco = str(senhaDoBanco)
            if senhaDoBanco != loginPassword:
                flash('Senha Incorreta, tente novamente')
                return redirect(url_for('register'))
        else:
            flash('Usuário não existe, troque para o menu de registro')
            return redirect(url_for('register'))  
    
    return redirect(url_for('index'))

@app.route("/success")
def success(): 
    return render_template('login_success.html')