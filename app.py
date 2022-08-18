from crypt import methods
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask("project")
app.secret_key = "ASFAFQER#r#@r@#$r%$t@$gtgdfadfadfeaf"

@app.route("/")
def hello():
  name = "robson"
  products = [
    {"nome": "Ração", "preço": 500},
    {"nome": "Ração", "preço": 500},
  ]
  return render_template("alo.html", n=name, p = products), 200

@app.route('/teste')
@app.route('/teste/<variavel>/<one>')
def funcao_teste(variavel = "", one = ""):
  x = int(variavel) + int(one)
  return "Teste new robson {}".format(x), 200

@app.route('/form')
def form():
  return render_template("form.html"), 200

@app.route('/form_recebe', methods=["POST", "GET"])
def form_recebe():
  nome = ""
  if request.method == "POST":
    nome = request.form["nome"]
    return f"Nome: {nome}", 200
  return "Só pode post buceta"

@app.route('/login')
def login():
  return render_template("login.html"), 200

@app.route('/login_validar', methods=["POST"])
def login_validar():
  if request.form["usuario"] == "z" and request.form["senha"] == "12345":
    session["usuario"] = request.form["usuario"]
    session["codigo"] = 1
    return redirect(url_for("acesso_restrito"))
  else:
    return "Usuário ou senha inválidos", 200
  
@app.route("/restrito")
def acesso_restrito():
  if session["codigo"] == 1:
    return "Bem-vindo à area restrita!!<br>Usuário: {}<br>Código: {}".format(session["usuario"], session["codigo"]), 200
  else:
    return "Acesso inválido", 200
    

app.run()