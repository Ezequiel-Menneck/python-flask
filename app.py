from flask import Flask, render_template
app = Flask("project")

@app.route("/")
def hello():
  return render_template("alo.html"), 200

app.run()