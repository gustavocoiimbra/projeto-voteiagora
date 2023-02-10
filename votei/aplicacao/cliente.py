from aplicacao import app
from flask import redirect, url_for, render_template, request
from aplicacao.user import User


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/registration', methods=["POST", "GET"])
def registration():
    if request.method == "POST":
        first = request.form["first"].lower().strip()
        last = request.form["last"].lower().strip()
        birth = request.form["birth"].strip()
        email = request.form["email"].lower().strip()
        gender = request.form["gender"].upper().strip()
        state = request.form["state"].upper().strip()
        usr = request.form["usr"].lower().strip()
        pwd = request.form["pwd"]
        all_var = [first, last, birth, email, state, usr, pwd]
        for var in all_var:
            if var == "":
                return redirect(url_for("alert"))
        user = User(first, last, usr, pwd, birth, email, gender, state)
        #print(first, last, birth, email, gender, state, usr, pwd)
        return redirect(url_for("search"))#, username = user.firstName)
    else:
        return render_template('registration.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        usr = request.form["usr"]
        pwd = request.form["pwd"]
        return redirect(url_for("search"))
    else:
        return render_template('login.html')


@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/alert')
def alert():
    return render_template('alert.html')

@app.route('/empty')
def empty():
    return render_template('empty.html')

@app.route('/<usr>')
def user(usr):
    return f"Olá, {usr}!"