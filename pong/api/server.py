from flask import Flask, render_template

app = Flask(__name__, template_folder = "templates")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name = name)

app.run(host = "localhost", port = "5002")