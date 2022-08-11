from flask import Flask, render_template
app = Flask("project")

@app.route("/")
def hello():
  name = "robson"
  products = [
    {"nome": "Ração", "preço": 500},
    {"nome": "Ração", "preço": 500},
  ]
  return render_template("alo.html", n=name, p = products), 200

app.run()