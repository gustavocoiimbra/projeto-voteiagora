from aplicacao import app
from flask import redirect, url_for, render_template, request, session
from datetime import timedelta
from user import User

app.secret_key = "B16BK3ecidwjMH1IezED"
app.permanent_session_lifetime = timedelta(minutes=5)


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
                warningPhrase = "Você não pode deixar nenhum campo em branco!"
                return redirect(url_for("warning", variable=warningPhrase))
        user = User(first, last, usr, pwd, birth, email, gender, state)
        #print(first, last, birth, email, gender, state, usr, pwd)
        return redirect(url_for("login"))#, username = user.firstName)
    else:
        return render_template('registration.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        usr = request.form["usr"]
        pwd = request.form["pwd"]
        print(usr, pwd)
        if not ( usr == "" or pwd == "" ):
            print("teste")
            session["user"] = usr
        return redirect(url_for("search"))
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route('/search')
def search():
    if "user" in session:
        print("teste2")
        print(session)
        userlogged = session["user"]
        print(userlogged)
        return render_template('search.html')
    else:
        if "user" in session:
            return redirec(url_for("search"))
        return redirect(url_for("login"))


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/warning/<variable>')
def warning(variable):
    print(variable)
    return render_template('warning.html', warningPhrase=variable)


@app.route('/empty')
def empty():
    return render_template('empty.html')


@app.route('/<usr>')
def user(usr):
    return f"Olá, {usr}!"