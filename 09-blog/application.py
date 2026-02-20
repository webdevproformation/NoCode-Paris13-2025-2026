from flask import Flask , render_template



application = Flask(__name__)



@application.route("/")
def home():
    return render_template("front/index.html")


