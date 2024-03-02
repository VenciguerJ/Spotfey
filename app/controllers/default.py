from app import app
from flask import render_template, request

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/login")
def italo_gay():
    return render_template('login.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit_data():
  if request.method == 'POST':
        # Obter os dados do formulário
        name = request.form['form_name']
        return render_template('teste.html', name = name)