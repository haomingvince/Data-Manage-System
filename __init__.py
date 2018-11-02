from flask import Flask, redirect, url_for, request, render_template
from model import *
from wtforms import Form, StringField, PasswordField, validators
# app = Flask(__name__)


class myForm(Form):
    username = StringField("username", [validators.required()])
    password = PasswordField("password", [validators.required()])


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    myform = myForm(request.form)
    if request.method == 'POST':
        usr = User(myform.username.data, myform.password.data)
        if usr.chkPwd() == 1:
            return redirect('https://www.bilibili.com')
        else:
            msg = 'login failed. Please check.'
            return render_template('index.html', message=msg, myform=myform)
    return render_template('index.html', myform=myform)


@app.route('/register', methods=['POST', 'GET'])
def register():
    myform = myForm(request.form)
    msg = ""
    if request.method == 'POST':
        usr = User(myform.username.data, myform.password.data)
        if usr.ifExist() == 1:
            msg = 'user already exist!'
        else:
            usr.add()
            msg = 'register successfully. Please re-login.'
    return render_template('index.html', message=msg, myform=myform)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    myform = myForm(request.form)
    msg = ""
    if request.method == 'POST':
        usr = User(myform.username.data, myform.password.data)
        if usr.chkPwd() == 1:
            usr.delete(myform.username.data)
            msg = 'Successfully deleted.'
        else:
            msg = 'login failed. Please check.'
    return render_template('index.html', message=msg, myform=myform)


@app.route('/update', methods=['POST', 'GET'])
def update():
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        origpwd = request.form['origpwd']
        newpwd = request.form['newpwd']
        usr = User(username, origpwd)
        if usr.chkPwd() == 1:
            usr.update(username, newpwd)
            msg = 'Successfully updated.'
        else:
            msg = 'login failed. Please check.'
    return render_template('admin.html', message=msg)


if __name__ == '__main__':
    app.run()
