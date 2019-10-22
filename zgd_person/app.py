import datetime
import time
import models
from flask import Flask
from form import LoginForm
from flask import render_template
from flask import request,redirect
from flask import url_for,flash
from flask import session
from flask import make_response

app = Flask(__name__)

@app.route('/hello')
def hello():
    pass
    name = request.args.get('name','Flask')
    return 'Hello %s'%name
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method=='POST':
        user = request.values.get('user')
        pwd = request.values.get('pwd')
        return 'hello world'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method=='POST':
        user = request.values.get('user')
        pwd = request.values.get('pwd')
        pwd2 = request.values.get('pwd2')
        if user:
            if pwd == pwd2:
                pass
        return redirect('/login')

# app.secret_key = 'SET_ME_BEFORE_USER_SESSION'
app.secret_key = 'secret string'
@app.route('/flush')
def flush():
    flash('I am Flash')

    return redirect(url_for('login'))
@app.route('/index')
def index():
    session['key_time'] = datetime.datetime.now().strftime('%Y-%m-%d')
    return session['key_time']
@app.route('/read/<int:year>')
def read(year):
    return 'Welcome to %s'%year
    # return session.get('key_time')
@app.route('/rend')
def renders():
    return '',302,{'Location':"hello"}
# with app.test_request_context():
#     print(url_for('hello'))
#     print(url_for('login'))
@app.route('/set/<name>')
def set_cook(name):
    response = make_response(url_for('hello'))
    response.set_cookie('name',name)
    return response
@app.route('/ser')
def ser_session():
    if 'logged_in' in session:
       return  'Welcome'

if __name__ == '__main__':
    app.run()
