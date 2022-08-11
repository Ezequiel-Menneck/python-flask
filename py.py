from flask import Flask 
app = Flask("project")

@app.route("/")
def hello():
  return "Salve garaio"

app.run()