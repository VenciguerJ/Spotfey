from flask import render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from app import app
from werkzeug.utils import secure_filename
from app.controllers.config import User
import os

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

#ROTAS
@app.route("/")
def index():
    from app.controllers.config import Musica
    from app.models.database_config import return_last_music

    ultimaMusica = return_last_music()
    print(ultimaMusica.Nome)
    if current_user.is_authenticated:
        current_username = current_user.username
        return render_template('index.html', current_username = current_username)    
    else:
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
        if  len(email) <= 0:
            flash('Insira um e-mail!')
            return redirect(url_for('register'))
        if len(email) > ConstUsers.MAX_CARACTERES_EMAIL:
            flash(f'Email muito grande, máximo suportado: {ConstUsers.MAX_CARACTERES_EMAIL}')
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
            caminhoArquivo = str(config.DEFAULT_PROFILE_IMAGE)

        # Se todas as validações passarem
        msg = cadastra_user(user, definitivePassword, email, caminhoArquivo)
        msg = str(msg)
        return render_template('login_success.html', msg=msg, profiledir=config.HTML_SOURCE_IMAGE, nome=user)
    
    return render_template('login.html')
      
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        loginUser = request.form['user-form-login']
        loginPassword = request.form['password-form-login']
        user = User.authenticate(loginUser, loginPassword)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas, verifique')
            return redirect(url_for('login'))     
        
    return render_template('login.html')

@app.route("/success")
def success():  
    return render_template('login_success.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/innermusic", methods=['GET', 'POST'])
@login_required
def innermusic():
    from app.controllers import config, utils
    from datetime import date
    from app.models.database_config import add_music, verifica_musica_existente

    if request.method == 'POST':
        # salvando as informações do form
        nomeMusica = request.form['form-nome-musica']
        arquivoMusica = request.files['form-arquivo-musica']
        fotoMusica = request.files['form-imagem-musica']

        # validando as informaçoes de texto
        if len(nomeMusica) > utils.ConstContent.MAX_CARACTERES_TEXTOS:
            flash(f'O nome "{nomeMusica}" muito grande, máximo de até 100 caracteres')
            return redirect(url_for('innermusic'))
        if len(nomeMusica) <= 0:
            flash('É preciso colocar um nome em sua música')
            return(redirect(url_for('innermusic')))
        
        if verifica_musica_existente(nomeMusica):
            flash('Esse nome de música já existe, tente um novo nome')
            return(redirect(url_for('innermusic')))
        
        #validação dos arquivos

        #cria diretório se não existir
        if not os.path.exists(os.path.join(config.Config.UPLOAD_MUSICS, current_user.username)):
            os.mkdir(os.path.join(config.Config.UPLOAD_MUSICS, current_user.username))
        
        # começa processo quando tiver aqrquivo da musica
        if arquivoMusica:
            nomeArquivoMusica = secure_filename(nomeMusica + os.path.splitext(arquivoMusica.filename)[1])

            if utils.valida_arquivo_musica(nomeArquivoMusica):
                caminhoArquivoMusica = os.path.join(config.Config.UPLOAD_MUSICS, current_user.username)

                utils.verifica_arquivo_dupicado(nomeArquivoMusica, caminhoArquivoMusica)
                
                #caminho do banco do arquivo mp3
                databaseArquivoMusica = os.path.join(caminhoArquivoMusica, nomeArquivoMusica)
                arquivoMusica.save(databaseArquivoMusica)
                
                #formata o dia para o banco
                dataAtual = date.today()
                stringData = dataAtual.strftime('%Y-%m-%d')

                #começa o processo se tiver foto 
                if fotoMusica:
                    nomeFoto = secure_filename('IMG' + nomeMusica + os.path.splitext(fotoMusica.filename)[1])
                    
                    if utils.valida_arquivo(nomeFoto):
                        utils.verifica_arquivo_dupicado(nomeFoto, os.path.join(config.Config.UPLOAD_MUSICS, current_user.username))

                        caminhoFotoMusica = os.path.join(config.Config.UPLOAD_MUSICS, current_user.username, nomeFoto)

                        fotoMusica.save(caminhoFotoMusica)

                        resultado = add_music(nomeMusica, current_user.iduser, stringData, databaseArquivoMusica, caminhoFotoMusica)

                        print(f'Resultado colocando foto: {resultado}')
                        
                        return render_template('preview_music.html', resultado=resultado, caminhoarquivo=caminhoFotoMusica, nome=nomeMusica)
                    else:
                        flash('Foto possui uma extensão de arquivo não suportada, coloque outra foto')
                        return redirect(url_for('innermusic'))
                #caso não tenha foto
                else:
                    fotoMusica = config.Config.HTML_SOURCE_IMAGE

                    print(fotoMusica)

                    resultado = add_music(nomeMusica, current_user.iduser, stringData, databaseArquivoMusica, fotoMusica)
                    
                    print(f'Resultado Sem colocar foto: {resultado}')
                    
                    return render_template('preview_music.html', resultado=resultado, caminhoarquivo=fotoMusica, nome=nomeMusica)
            else:
                flash('Extensão de arquivo não suportada\n')
                return redirect(url_for('innermusic'))
        else:
            flash('Não se esqueça de colocar a música!')
            return redirect(url_for('innermusic'))

    return render_template('inner_music.html')