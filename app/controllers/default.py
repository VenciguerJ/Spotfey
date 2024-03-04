from app import app
from flask import Flask, render_template, request
# from _mysql_connector import db

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/login")
def italo_gay():
    return render_template('login.html', error_message=None)

@app.route("/submit", methods=['GET', 'POST'])
def submit_data():

  if request.method == 'POST':
        # Obter os dados do formulário
        name = request.form['form_name']
        user = request.form['form_user']
        password = request.form['form_password']
        confirm_password = request.form['form_confirm_password']
        type1 = request.form.get('form_type_1', 'off')
        type2 = request.form.get('form_type_2', 'off')

        #Definindo valores
        db_normal_user = int(1)
        db_artist_user = int(2)
        typeUser = None

        #validação
        if type1 == 'on' and type2 == 'off':
            typeUser = db_normal_user
        elif type1 == 'off' and type2 == 'on':
            typeUser = db_artist_user
        elif type1 == 'on' and type2 == 'on':
            typeUser = db_artist_user
        else:
            error_message = 'Marque ao menos uma das alternativas na seção "Perguntas de usuário"'
            return render_template('login.html', error_message=error_message)


        if password != confirm_password:
            error_message = 'senhas não condizem, tente novamente'
            return render_template('login.html', error_message=error_message)


        #Submit
        return render_template(
            'teste.html',
            name = name, 
            user=user,
            password=password,
            confirm=confirm_password,
            typeUserDB=typeUser
        )