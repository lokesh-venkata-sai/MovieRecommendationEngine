from flask import Flask, request, render_template, url_for, session, redirect, g
from login import login
from register import register
import os
from homefile import homefile
from datetime import timedelta
import pymysql
from interestfile import update
from moviesfile import moviefile

app = Flask(__name__)


# app.config.from_pyfile("config.cfg")
@app.route('/')
@app.route('/<login>')
def index(login=None):
    return render_template("index.html", login=login)


@app.route('/signup.html')
def signup():
    return render_template("signup.html")


@app.route('/loginForm', methods=['GET', 'POST'])
def loginForm():
    result = request.form
    x = login()
    y = x.validateLogin(**result)
    if request.method == 'POST':
        session.pop('mail', None)
        if y == True:
            session['mail'] = result['mailId']

            return redirect(url_for('home'))
    return render_template("index.html", login=True)


@app.route('/home')
def home():
    if g.mail:  # to check if logged in
        y = homefile()  # not yet implemented
        results = y.homefunc()
        return render_template('home.html', results=results)
    return redirect(url_for('index'))

@app.route('/movies')
def movies():
    if g.mail:  # to check if logged in
        obj=moviefile()
        results=obj.moviesfunc()
        print(len(results))
        print(type(results))
        return render_template('Movies.html',results=results,length=len(results))
    return redirect(url_for('index'))

@app.route('/registerForm', methods=['GET', 'POST'])
def registerForm():
    result = request.form
    genre = result.getlist('genre')
    ob = register()
    print(genre)
    ans = ob.registerfunc(*genre, **result)
    email = result['mailId']
    if ans == True:
        status = True
        return render_template("signup.html", status=status)
    else:
        return render_template("signup.html", status=False)


@app.route('/myprofile', methods=['GET', 'POST'])
def myprofile():
    if g.mail:
        user = session.get("mail")
        db = pymysql.connect("localhost", "root", "lokesh1999", "movieRecommendataion")
        cursor = db.cursor()
        sql = "select * from users where email=%s"
        value = (session.get("mail"))
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            user = cursor.fetchall()
            # print(user)
        except:
            print("Error: unable to fetch data")
        db.close()
        print("user values:", user)
        return render_template("myprofile.html", user=user)
    return redirect(url_for('index'))


@app.route('/interestForm', methods=['GET', 'POST'])
def interestForm():
    result = request.form
    genre = result.getlist('genre')
    obj = update()
    ans = obj.updatefunc(*genre, **result)
    return redirect(url_for('myprofile'))


@app.before_request
def before_request():
    g.mail = None
    if 'mail' in session:
        g.mail = session['mail']
        print("hi ", g.mail)


@app.route('/getsession')
def getsession():
    if 'mail' in session:
        return session['mail']
    return 'Not logged in!'


@app.route('/dropsession')
def dropsession():
    session.pop('mail', None)
    return render_template("index.html")


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.permanent_session_lifetime = timedelta(minutes=10)
    app.run(debug=True)
    #app.run(debug=True,host="0.0.0.0")
