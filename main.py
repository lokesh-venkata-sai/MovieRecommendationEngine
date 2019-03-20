from flask import Flask, request, render_template, url_for, session,redirect,g
from login import login
from register import register
import os
from homefile import homefile


app = Flask(__name__)

#app.config.from_pyfile("config.cfg")
app.secret_key=os.urandom(24)


@app.route('/')
@app.route('/<login>')
def index(login=None):
    session.pop('mailId', None)
    return render_template("index.html",login=login)


@app.route('/signup.html')
def signup():
    return render_template("signup.html")

@app.route('/home')
def home():
    if g.mailId:
        print("home ",g.mailId)
        y=homefile()
        results=y.homefunc()
        return render_template('home.html',results=results)
    return redirect(url_for('index'))

@app.route('/loginForm',methods = ['GET','POST'])
def loginForm():
    result=request.form
    x = login()
    y=x.validateLogin(**result)
    if y==True:
        session.pop('mailId',None)
        session['mailId'] = result['mailId']
        return redirect(url_for('home'))
    else:
        return render_template("index.html",login=True)



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
    if g.mailId:
        print(session.get("mailId"))
        user=session.get("mailId")
        return render_template("myprofile.html",user=user)
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.mailId=None
    if 'mailId' in session:
        g.mailId=session['mailId']
        print("hi ",g.mailId)

@app.route('/getsession')
def getsession():
    if 'mailId' in session:
        return session['mailId']
    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('mailId', None)
    return render_template("index.html")




if __name__=="__main__":
    app.run(debug=True)