import models
import stores
from flask import Flask, render_template

app = Flask(__name__)

post_store = stores.PostStore()

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/SayHello/<name>")
def say_hellow(name):
    return "Hello {name}".format(name=name)


app.run()
