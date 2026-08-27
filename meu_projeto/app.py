import re
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect
import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # Não envia dados de verdade, apenas conecta a um IP externo fictício
    s.connect(("8.8.8.8", 80))
    ipv4_correto = s.getsockname()[0]
finally:
    s.close()

print(f"IP Local Correto: {ipv4_correto}")


PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_BASE, "instance", "banco.db")

def start_db():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            observacao TEXT,
            linguagens_string TEXT NOT NULL,
            turno TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            id INTEGER PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT id FROM config LIMIT 1")
    config = cursor.fetchone()

    senha_hash = generate_password_hash("senhamirabolante")

    if config is None:
        cursor.execute("""
            INSERT INTO config (id, password)
            VALUES (?, ?)
        """, (1, senha_hash))
    
    conexao.commit()
    conexao.close()

start_db()

app = Flask(__name__)

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
SENHA_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\-_@!#$%^&*()=+])[A-Za-z\d\-_@!#$%^&*()=+]{8,}$'
estados_permitidos = ['sp','rj','mg','df','ba','ce','pr','pe']
linguagens_permitidas = ['python','java','js','html','css']
turnos_permitidos = ['manha','tarde','noite']

@app.route("/", methods = ["GET","POST"])
def cadastro():
    if request.method =="POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        observacao = request.form["observacao"]
        turno = request.form.get("turno")
        linguagens = request.form.getlist("linguagem")
        estado = request.form.get("estado")
        

        #validacao njome
        if nome.strip() =="":
            return "nome invalido!"
        
        #validacao idade
        try:
            idade = int(request.form["idade"])
        except ValueError:
            return "idade invalida!"
        if idade <= 0 or idade > 120:
            return "idade invalida!"
        
        #validacao email
        if not re.match(EMAIL_REGEX,email):
            return 'email invalido!'
        
        #validar a senha
        if not re.match(SENHA_REGEX, senha):
            return f'A senha deve conter:\nPelo menos uma letra minuscula(a/z)\nPelo menos uma letra maiuscula(A-Z)\nPelo menos um digito\nPelo menos um simbolo(@,#,&...)\nPelo menos 8 caracteres'
        #validar obs
        if not observacao.strip():
            observacao = "Nenhuma observacao"

        #validar turno
        if not turno:
            return 'Voce precisa selecionar um turno!'
        if turno not in turnos_permitidos:
            return 'Turno invalido! (Turnos permitidos: Manha,Tarde,Noite)'
        
        #validar linguagens
        if not linguagens:
            return 'voce deve escolher uma linguagem!'
        for linguagem in linguagens:
            if linguagem not in linguagens_permitidas:
                return 'Voce deve escolher "Python" , "HTML" ou "CSS"'

        #validar estado
        if estado =='':
            return 'selecione uma opcao!'
        if estado not in estados_permitidos:
            return 'selecione uma opcao na lista de selecao!'

        #Integracao banco de dados 

        linguagens_string = ",".join(linguagens)

        conexao = sqlite3.connect(CAMINHO_BANCO)
        cursor = conexao.cursor()

        #hash

        senha_hash = generate_password_hash(senha)

        try:
            cursor.execute("""INSERT INTO usuarios(nome,idade,email,senha,observacao,linguagens_string,turno,estado)
            VALUES(?,?,?,?,?,?,?,?)""",(
            nome,idade,email,senha_hash,observacao,linguagens_string,turno,estado))

            conexao.commit()

        except sqlite3.IntegrityError:
            conexao.close()
            return 'Esse email ja esta sendo usado!'
        cursor.execute("SELECT * FROM usuarios")
               
        resultados = cursor.fetchall()
        print(resultados)
        conexao.close()
        

        return redirect("/inicio")
        
    return render_template("index.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/voltar", methods = ["GET","POST"])
def voltar():
    if request.method =="POST":
        return redirect("/")

@app.route("/voltar_ini", methods = ["GET","POST"])
def voltar_ini():
    if request.method =="POST":
        return redirect("/inicio")

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method =='POST':
        return redirect("/")

@app.route("/banco", methods =['GET','POST'])
def mostrar_banco():    
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios ")
    resultados = cursor.fetchall()
    print(resultados)

    return render_template("banco.html", tabela=resultados)

@app.route("/enviar-validacao", methods =['GET','POST'])
def validacao():
    if request.method == "POST":

        conexao = sqlite3.connect(CAMINHO_BANCO)
        cursor = conexao.cursor()

        cursor.execute("SELECT password FROM config")
        password_hash = cursor.fetchone()[0]

        password = request.form.get("password")

        if check_password_hash(password_hash, password): 
            cursor.execute("DELETE FROM usuarios")
            conexao.commit()
            conexao.close()

            return redirect("/inicio")
        
        else:
            conexao.close()
            return "Senha invalida!"
        
    return render_template("excluir-banco-validacao.html")

app.run(debug=True,
        host='0.0.0.0', 
        port=5000)
