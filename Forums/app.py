import models
import stores
from flask import Flask, render_template

app = Flask(__name__)

post_store = stores.PostStore()
post_store.add(models.Post("Life", "Life is alawys great"))
post_store.add(models.Post("Sunshine", "Sunshine is amazing"))


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_store.get_all())


@app.route("/SayHello/<name>")
def say_hellow(name):
    return "Hello {name}".format(name=name)


app.run()
