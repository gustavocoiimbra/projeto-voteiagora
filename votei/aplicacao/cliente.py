from aplicacao import app #, db
from flask import redirect, url_for, render_template, \
    request, session, flash
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
        pwd_check = request.form["pwd2"]
        all_var = [first, last, birth, email, state, usr, pwd]
        errorRegistration = False
        for var in all_var:
            if var == "":
                errorRegistration = True
                flash("Você não pode deixar nenhum campo em branco!")
                break
        if pwd != pwd_check:
            flash("Senhas não coincidem!")
            errorRegistration = True
        if errorRegistration:
            return render_template('registration.html')
            #warningPhrase = "Você não pode deixar nenhum campo em branco!"
            #return redirect(url_for("warning", variable=warningPhrase))
            
        user = User(first, last, usr, pwd, birth, email, gender, state)
        #print(first, last, birth, email, gender, state, usr, pwd)
        flash("Cadastro Realizado! Faça o login.")
        return redirect(url_for("login"))#, username = user.firstName)
    else:
        return render_template('registration.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        usr = request.form["usr"]
        pwd = request.form["pwd"]
        if not ( usr == "" or pwd == "" ):
            session["user"] = usr
        else:
            flash("Você precisa entrar com usuário e senha!")
        return redirect(url_for("search"))
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Você saiu do sistema!", "info")
    return redirect(url_for("login"))


@app.route('/search')
def search():
    if "user" in session:
        userlogged = session["user"]
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
    #print(variable)
    return render_template('warning.html', warningPhrase=variable)


#@app.route('/<usr>')
#def user(usr):
#    return f"Olá, {usr}!"