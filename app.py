from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>opa<h1><p> povo<p>'

@app.route('/aluno')
def alunos():
    return 'aluno'
