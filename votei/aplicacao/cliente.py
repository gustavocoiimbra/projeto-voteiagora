from aplicacao import app
from flask import redirect, url_for, render_template, \
    request, session, flash
from aplicacao.user import User
from aplicacao.dataUsersControl import writeData
from aplicacao import allUsers
from aplicacao import allCandidatos


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
        print(allUsers)
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

        allUsers.append(User(first, last, usr, pwd, birth, email, \
                             gender, state))
        writeData(allUsers)

        flash("Cadastro Realizado! Faça o login.")
        return redirect(url_for("login"))  # , username = user.firstName)
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
                return redirect(url_for("search"))
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


@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == "POST":
        session.permanent = True
        buscando = request.form["buscando"]
        if buscando != "":
            return redirect(url_for("resultados"))
        flash("Digite o nome do candidato!")
        return render_template('search.html')
    else:
        return render_template('search.html')


@app.route('/resultados', methods=["GET"])
def resultados():

    # Lista com os candidatos que foram encontrados
    obj = ['Candidato X', 'Candidato Y', 'Candidato Z']

    return render_template('resultados.html', obj=obj)


@app.route('/candidato/<nome>', methods=["GET"])
def candidato(nome):

    for i in range(len(allCandidatos)):
        if allCandidatos[i].name.lower() == nome.lower():
            obj = {
                'name': allCandidatos[i].name,
                'partido': allCandidatos[i].partido,
                'cargo': allCandidatos[i].cargo,
                'inicioMandato': allCandidatos[i].inicioMandato,
                'fimMandato': allCandidatos[i].fimMandato,
                'estado': allCandidatos[i].estado,
                'propostasLegs': allCandidatos[i].propostasLegs
            }
            return render_template('candidato.html', obj=obj)


@app.route('/aboutus', methods=["GET"])
def aboutus():
    return render_template('aboutus.html')


@app.route('/contact', methods=["GET"])
def contact():
    return render_template('contact.html')


@app.route('/base', methods=["GET"])
def base():
    return render_template('base.html')


@app.route('/warning/<variable>', methods=["GET"])
def warning(variable):
    # print(variable)
    return render_template('warning.html', warningPhrase=variable)

# @app.route('/<usr>')
# def user(usr):
#    return f"Olá, {usr}!"
