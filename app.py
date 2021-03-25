from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    name = "Farrah"
    return render_template("home.html",user_name=name)

@app.route('/about')
def about_page():
    return render_template("about.html",)



