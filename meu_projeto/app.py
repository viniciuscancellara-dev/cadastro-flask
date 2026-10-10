import re
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import os
from dotenv import load_dotenv
from functools import wraps

load_dotenv()

PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_BASE, "instance", "banco.db")

def start_db():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    #usuarios cadastrados
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
    #deletar id
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            id INTEGER PRIMARY KEY,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("SELECT id FROM config LIMIT 1")
    config = cursor.fetchone()

    if config is None:
        hash = os.getenv("DELETE_HASH")
        if not hash:
            raise ValueError('erro: a variavel hash (env) nao foi carregada corretamente!') 
           
        senha_hash = generate_password_hash(hash)

        cursor.execute("""
            INSERT INTO config (id, password)
            VALUES (?, ?)
        """, (1, senha_hash))

    #login

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login (
        id INTEGER PRIMARY KEY,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL)
    """)

    conexao.commit()
    conexao.close()

start_db()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
SENHA_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\-_@!#$%^&*()=+])[A-Za-z\d\-_@!#$%^&*()=+]{8,}$'
NOME_REGEX = r"^[A-Za-zÀ-ÿ\s]+$"
estados_permitidos = ['sp','rj','mg','df','ba','ce','pr','pe']
linguagens_permitidas = ['python','java','js','html','css']
turnos_permitidos = ['manha','tarde','noite']

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logado' not in session:
            return redirect("/")
        return func(*args, **kwargs)
    return wrapper

@app.errorhandler(404)
def Page404(erro):
    if 'logado' in session:
        return render_template('404.html',
                               logado=True),404
    else:
        return render_template('404.html',
                               logado=False),404

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        usuario_digitado = request.form.get("usuario")
        senha_digitada = request.form.get("senha")
        
        conexao = sqlite3.connect(CAMINHO_BANCO)
        cursor = conexao.cursor()

        cursor.execute("SELECT id, usuario, senha FROM login WHERE usuario = ?", (usuario_digitado,))
        resultado = cursor.fetchone()

        cursor.execute("SELECT usuario FROM login")
        print("USUARIOS NO BANCO:", cursor.fetchall())

        print("USUARIO:", usuario_digitado)
        print("SENHA:", senha_digitada)
        print("RESULTADO:", resultado)

        if resultado is None:
            conexao.close()

            return jsonify({
                "sucesso": False,
                "mensagem": "Usuário ou senha incorretos!"
            })


        id_banco = resultado[0]
        hash_banco = resultado[2]

        conexao.close()

        if not check_password_hash(hash_banco, senha_digitada):
            return jsonify ({
                "sucesso": False,
                "mensagem": "Usuário ou senha incorretos!"
            })

        session["logado"] = True
        session["usuario"] = usuario_digitado
        session["usuario_id"] = id_banco

        session.permanent = False

        return jsonify({
            "sucesso":True,
            "mensagem":"Login bem sucedido",
            "redirect":"/inicio"
        })

    return render_template("login.html")

@app.route("/sign", methods=["GET", "POST"])
def sign():
  
    if request.method =="POST":
    
        conexao = sqlite3.connect(CAMINHO_BANCO)
   
        cursor = conexao.cursor()

        user = request.form.get("user")
        userPassword = request.form.get("userPassword")

        #validando inputs
        if not user or user.strip() == "":
            return jsonify({
                "sucesso":False,
                "mensagem": "O nome de usuario e obrigatorio!"
            })
        
        if user:
            user = user.strip()

        if not re.match(SENHA_REGEX, userPassword):
            return jsonify({
                "sucesso":False,
                "mensagem":"Senha invalida!"
            })

        #criando hash pra senha
        
        login_hash = generate_password_hash(userPassword)
      
        #insert no banco
        cursor.execute("SELECT id FROM login WHERE usuario=?", (user,))
        login = cursor.fetchone()
       
        if login is None:

            cursor.execute("""
                INSERT INTO login (usuario, senha)
                VALUES (?, ?)       
            """, (user, login_hash ))

            conexao.commit()
            conexao.close()

            return jsonify({
                "sucesso": True,
                "mensagem": "Usuario criado com sucesso!",
                "redirect":"/"
            })
            

        else:
            conexao.close()

            return jsonify({
                "sucesso":False,
                "mensagem": "Usuario ja cadastrado!"
            })
    return render_template("sign.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")

@app.route("/cadastrar", methods = ["GET","POST"])
@login_required
def cadastro():
    if request.method =="POST":
        nome = request.form.get("nome"," ").strip()
        email = request.form["email"]
        senha = request.form["senha"]
        observacao = request.form["observacao"]
        turno = request.form.get("turno")
        linguagens = request.form.getlist("linguagem")
        estado = request.form.get("estado")
        

        #validacao njome
        if not re.fullmatch(r"^[A-Za-zÀ-ÿ -]+", nome):
            return jsonify({
                "sucesso":False,
                "mensagem":"Nome invalido!"
            })
        
        #validacao idade
        try:
            idade = int(request.form.get("idade"))
        except ValueError:
            return jsonify({
                "sucesso":False,
                "mensagem":"Idade invalida"
            })
        if idade <= 0 or idade > 120:
            return jsonify({
                "sucesso":False,
                "mensagem":"Idade invalida"
            })
        
        #validacao email
        if not re.match(EMAIL_REGEX,email):
            return jsonify({
                "sucesso":False,
                "mensagem":"Email invalido!"
            })
        
        #validar a senha
        if not re.match(SENHA_REGEX, senha):
            return ({
                "sucesso":False,
                "mensagem":"Senha invalida!"
            })
        #validar obs
        if not observacao.strip():
            observacao = "Nenhuma observacao"

        #validar turno
        if not turno:
            return jsonify({
                "sucesso":False,
                "mensagem":"Insira um turno!"
            })
        if turno not in turnos_permitidos:
            return jsonify({
                "sucesso":False,
                "mensagem":"Turno invalido!"
            })
        
        #validar linguagens
        if not linguagens:
            return jsonify({
                "sucesso":False,
                "mensagem":"Escolha uma linguagem!"
            })
        for linguagem in linguagens:
            if linguagem not in linguagens_permitidas:
                return jsonify({
                    "sucesso":False,
                    "mensagem":"Escolha uma linguagem!"
                })

        #validar estado
        if estado =='':
            return jsonify({
                "sucesso":False,
                "mensagem":"Escolha um estado da lista"
            })
        if estado not in estados_permitidos:
            return jsonify({
                "sucesso":False,
                "mensagem":"Escolha um estado da lista"
            })

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
            return jsonify({
                "sucesso":False,
                "mensagem": "Email ja cadastrado!"
            })
        cursor.execute("SELECT * FROM usuarios")
               
        resultados = cursor.fetchall()
        print(resultados, flush=True)
        conexao.close()
        

        return jsonify({
            "sucesso":True,
            "mensagem":"Usuario cadastrado!",
            "redirect":"/inicio",
        })
        
    return render_template("index.html")

@app.route("/inicio")
@login_required
def inicio():
    return render_template("inicio.html")

@app.route("/voltar", methods = ["GET","POST"])
@login_required
def voltar():
    if request.method =="POST":
        return redirect("/cadastrar")

@app.route("/voltar_ini", methods = ["GET","POST"])
@login_required
def voltar_ini():
    if request.method =="POST":
        return redirect("/inicio")

@app.route("/add", methods=['GET','POST'])
@login_required
def add():
    if request.method =='POST':
        return redirect("/cadastrar")

@app.route("/banco", methods =['GET','POST'])
@login_required
def mostrar_banco():    
    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios ")
    resultados = cursor.fetchall()
    print(resultados)

    conexao.close()

    return render_template("banco.html", tabela=resultados)

@app.route("/editar", methods=["POST"])
@login_required
def editar():
    id_usuario = request.form.get("id")
    nome = request.form.get("nome", "")
    observacao = request.form.get("observacao", "")
    turno = request.form.get("turno")
    linguagens = request.form.getlist("linguagem")
    estado = request.form.get("estado")

    #validacao id
    if not id_usuario:
        return "usuario invalido!"

    #validacao nome
    if nome.strip() == "":
        return "nome invalido!"

    #validacao idade
    try:
        idade = int(request.form["idade"])
    except ValueError:
        return "idade invalida!"
    if idade <= 0 or idade > 120:
        return "idade invalida!"

    #validacao email
    email = request.form.get("email", "")
    if not re.match(EMAIL_REGEX, email):
        return jsonify({
            "sucesso":False,
            "mensagem":"Email invalido"
        })

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
    if estado == '':
        return 'selecione uma opcao!'
    if estado not in estados_permitidos:
        return 'selecione uma opcao na lista de selecao!'

    #Atualizacao no banco (senha NAO e alterada)

    linguagens_string = ",".join(linguagens)

    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()

    try:
        cursor.execute("""UPDATE usuarios
            SET nome = ?, idade = ?, email = ?, observacao = ?, linguagens_string = ?, turno = ?, estado = ?
            WHERE id = ?""",(
            nome, idade, email, observacao, linguagens_string, turno, estado, id_usuario))

        conexao.commit()

    except sqlite3.IntegrityError:
        conexao.close()
        return 'Esse email ja esta sendo usado!'

    conexao.close()

    return jsonify({
            "sucesso":True,
            "mensagem":"Usuario editado com sucesso!",
        })

@app.route("/enviar-validacao", methods=["GET", "POST"])
@login_required
def validacao():
    if request.method == "GET":
        conexao = sqlite3.connect(CAMINHO_BANCO)
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()

        conexao.close()

        return render_template("excluir-banco-validacao.html",tabela=resultados)

    conexao = sqlite3.connect(CAMINHO_BANCO)
    cursor = conexao.cursor()
    if request.method == "POST":
        try:
            if "password" in request.form:
                cursor.execute("SELECT password FROM config")
                result = cursor.fetchone()

                if not result:
                    return jsonify({
                        "sucesso": False,
                        "mensagem": "ERRO! Senha nao gerada!"
                    })

                password_hash = result[0]
                password = request.form.get("password")

                if check_password_hash(password_hash, password):
                    session["pode_excluir_usuario"] = True

                    return jsonify({
                        "sucesso": True
                    })

                return jsonify({
                    "sucesso": False,
                    "mensagem": "Senha invalida."
                })

            if "id-excluir" in request.form:
                id_excluir = request.form.get("id-excluir", "").strip()

                if "pode_excluir_usuario" not in session:
                    return jsonify({
                        "sucesso": False,
                        "mensagem": "Validacao necessaria."
                    }), 403

                if not id_excluir:
                    return jsonify({
                        "sucesso": False,
                        "mensagem": "ID do usuario nao informado."
                    }), 400

                cursor.execute(
                    "DELETE FROM usuarios WHERE id = ?",
                    (id_excluir,)
                )

                if cursor.rowcount == 0:
                    return jsonify({
                        "sucesso": False,
                        "mensagem": "Usuario nao encontrado."
                    }), 404

                conexao.commit()

                return jsonify({
                    "sucesso": True,
                    "id": id_excluir
                })

            return jsonify({
                "sucesso": False,
                "mensagem": "Requisicao invalida."
            }), 400

        except sqlite3.Error as e:
            conexao.rollback()

            print("ERRO:", e)

            return jsonify({
                "sucesso": False,
                "mensagem": "Erro ao acessar o banco de dados."
            }), 500

        finally:
            conexao.close()

if __name__ == '__main__':
    debug = os.getenv('DEBUG_MODE','False').lower() == 'true'
    app.run(debug=debug,
            host='0.0.0.0', 
            port=5000)
