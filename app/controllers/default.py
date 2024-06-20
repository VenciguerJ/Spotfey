<<<<<<< HEAD
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app import app, config
import os

=======
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app import app
import os

from app.controllers import config

>>>>>>> 5b6e02677efb2eb2d84964daff6ebf6d266cef28
@app.route("/")
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/success', methods=['GET', 'POST'])
def successful_login():
    from app.models.database_config import cadastra_user
    from app.controllers.utils import valida_arquivo, verifica_arquivo_dupicado, ConstUsers

    CaminhoArquivo = None

    #registro
=======
@app.route("/register", methods=['GET', 'POST']) #contém os formulários de login e registro e redireciona o registro para a mesma pagina para logar
def register():
    from app.models.database_config import cadastra_user, verifica_usuario_existente
    from app.controllers.utils import valida_arquivo, verifica_arquivo_dupicado, ConstUsers



>>>>>>> 5b6e02677efb2eb2d84964daff6ebf6d266cef28
    if request.method == 'POST':
        user = request.form['form_user']
        email = request.form['form_email']
        password = request.form['form_password']
        fotoPerfil = request.files['form_profile_picture']
        password2 = request.form['form_password2']

<<<<<<< HEAD

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

    


=======
        # Validação de usuário
        print(verifica_usuario_existente(user))
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
        CaminhoArquivo = None
        if fotoPerfil:
            nomeArquivo = secure_filename('profile' + os.path.splitext(fotoPerfil.filename)[1])
            if valida_arquivo(nomeArquivo):
                CaminhoArquivo = os.path.join(config.Config.UPLOAD_IMAGES, user)
                if not os.path.exists(CaminhoArquivo):
                    os.makedirs(CaminhoArquivo)
                else:
                    verifica_arquivo_dupicado(nomeArquivo, CaminhoArquivo)
                fotoPerfil.save(os.path.join(CaminhoArquivo, nomeArquivo))
            else:
                flash('Extensão de arquivo não suportada')
                return redirect(url_for('register'))

        # Se todas as validações passarem
        msg = cadastra_user(user, definitivePassword, email, CaminhoArquivo)
        msg = str(msg)
        return render_template('login_success.html', msg=msg, sql=verifica_usuario_existente(user))
    
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
>>>>>>> 5b6e02677efb2eb2d84964daff6ebf6d266cef28
