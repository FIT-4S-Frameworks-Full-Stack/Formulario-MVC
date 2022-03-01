import os, sqlite3
from flask import Flask, render_template, request

# APLICAÇÃO FLASK
app = Flask(__name__)

# APLICAÇÃO SQLITE
conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE CADASTRO (USER_NAME TEXT, USER_EMAIL TEXT, USER_PASSWORD TEXT)')
conn.close()

# CONTROLLERS
@app.route('/')
def main():
    return render_template('signup.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    if nome and email and senha:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO CADASTRO (USER_NAME, USER_EMAIL, USER_PASSWORD) VALUES (?, ?, ?)', (nome, email, senha))
        conn.commit()
        return render_template('signup.html')

@app.route('/listar', methods=['POST', 'GET'])
def listar():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT USER_NAME, USER_EMAIL, USER_PASSWORD FROM CADASTRO')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='localhost', port=port, debug=True)
