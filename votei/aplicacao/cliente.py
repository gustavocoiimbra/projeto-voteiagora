from aplicacao import app #, db
from flask import redirect, url_for, render_template, \
    request, session, flash
from aplicacao.user import User
from aplicacao.dataUsersControl import writeData
from aplicacao import allUsers


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
        all_var = [first, last, birth, email, gender, state, usr, pwd]
        errorRegistration = False
        # Verificando se ha campos em branco
        for var in all_var:
            if var == "":
                errorRegistration = True
                flash("Você não pode deixar nenhum campo em branco!")
                break
        if pwd != pwd_check:
            flash("Senhas não coincidem!")
            errorRegistration = True

        # Verificando se usuario ja foi cadastrado
        for i in range(len(allUsers)):
            if email == allUsers[i].email:
                flash("E-mail já foi cadastrado!")
                errorRegistration = True
                break
            elif usr == allUsers[i].userName:
                flash("Nome de usuário já cadastrado!")
                errorRegistration = True
                break
        if errorRegistration:
            return render_template('registration.html')

        allUsers.append ( User(first, last, usr, pwd, birth, email, \
                                gender, state) )
        writeData(allUsers)
              

        flash("Cadastro Realizado! Faça o login.")
        return redirect(url_for("login"))#, username = user.firstName)
    else:
        return render_template('registration.html')


@app.route('/mydata')
def mydata():
    for i in range(len(allUsers)):
        if allUsers[i].userName == str(session["user"]):
            break
    return render_template('mydata.html', obj=allUsers[i])


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        usr = request.form["usr"]
        pwd = request.form["pwd"]
        for i in range(len(allUsers)):
            if allUsers[i].userName == usr and allUsers[i].password == pwd:
                session["user"] = usr
                return render_template("search.html")
        if usr == "" or pwd == "":
            flash("Você precisa entrar com usuário e senha!")
        else:
            flash("Usuário inexistente ou senha incorreta!")
        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Você saiu do sistema!", "info")
    return redirect(url_for("login"))


@app.route('/search', methods =["GET"] )
def search():
#   if "user" in session:
#      userlogged = session["user"]
#        pass
#    else:
#        if "user" in session:
#            return redirect(url_for("search"))
#        return redirect(url_for("login"))
    if request.method == "GET":
        session.permanent = True
        return render_template('search.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


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