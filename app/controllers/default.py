from flask import render_template, request, redirect, url_for
from app import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/success', methods=['GET', 'POST'])
def successful_login():
    from app.models.database_config import cadastra_user

    if request.method == 'POST':
        user = request.form['form_user']
        email = request.form['form_email']
        photo = request.form['form_profile_picture']
        password = request.form['form_password']
    
    msg = cadastra_user(user, password, email)
    msg = str(msg)

    return render_template('login_success.html', message=msg)