from flask import Flask, request, render_template, url_for, session,redirect,g
from login import login
from register import register
import os
from homefile import homefile
from datetime import timedelta

app = Flask(__name__)

#app.config.from_pyfile("config.cfg")

@app.route('/')
@app.route('/<login>')
def index(login=None):
    return render_template("index.html",login=login)


@app.route('/signup.html')
def signup():
    return render_template("signup.html")



@app.route('/loginForm',methods = ['GET','POST'])
def loginForm():
    result=request.form
    x = login()
    y=x.validateLogin(**result)
    if request.method == 'POST':
        session.pop('mail', None)
        if y==True:
            session['mail'] = result['mailId']
            return redirect(url_for('home'))
    return render_template("index.html",login=True)

@app.route('/home')
def home():
    if g.mail:
        y=homefile()
        results=y.homefunc()
        return render_template('home.html',results=results)
    return redirect(url_for('index'))



@app.route('/registerForm', methods = ['GET', 'POST'])
def registerForm():
        result=request.form
        ob=register()
        ans=ob.registerfunc(**result)
        email = result['mailId']
        if ans==True:
            status=True
            return  render_template("signup.html",status=status)
        else:
            return render_template("signup.html",status=False)


@app.route('/myprofile')
def myprofile():
    if g.mail:
        #print(session.get("mailId"))
        user=session.get("mail")
        return render_template("myprofile.html",user=user)
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.mail=None
    if 'mail' in session:
        g.mail=session['mail']
        print("hi ",g.mail)


@app.route('/getsession')
def getsession():
    if 'mail' in session:
        return session['mail']
    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('mail', None)
    return render_template("index.html")




if __name__=="__main__":
    app.secret_key = os.urandom(24)
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(debug=True)