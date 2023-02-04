from aplicacao import app
from flask import redirect, url_for, render_template, request


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/search')
def search():
    return "Olá, usuário!"

@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/<usr>')
def user(usr):
    return f"Olá, {usr}!"