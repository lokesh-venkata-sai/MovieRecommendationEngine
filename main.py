from flask import Flask, request, render_template, url_for, session, redirect, g
from login import login
from register import register
import os
from homefile import homefile
from datetime import timedelta
import pymysql
from interestfile import update
from moviesfile import moviefile
from singleMoviefile import singleMovie
from ratingfile import ratingfile
app = Flask(__name__)

mysql_server="localhost"
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
        user_id = ""
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select id from users where email=%s"
        value = (g.mail)
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            movie = cursor.fetchall()
            user_id = movie[0][0]
        except:
            print("Error: unable to fetch data")
        db.close()
        y = homefile()
        results = y.homefunc()
        recommend=y.getrecommend(user_id)
        if recommend == None:
            print("none")
            return render_template('home.html',results=results,novalue="")

        return render_template('home.html', results=results, results1=recommend)
    return redirect(url_for('index'))

@app.route('/movies',)
def movies():
    if g.mail:  # to check if logged in i.e to check session is on
        obj=moviefile()
        results=obj.moviesfunc()
        return render_template('Movies.html',results=results)
    return redirect(url_for('index'))

@app.route('/searchForm',methods=['GET', 'POST'])
def searchForm():
    if g.mail:
        inp = request.form
        search=inp['searching']
        movies=""
        if search!="":
            db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
            cursor = db.cursor()
            sql = "select * from movies where movie like %s"
            x="%"+inp['searching']+"%"
            value = (x)
            print("val - ",value)
            try:
                # Execute the SQL command
                cursor.execute(sql, value)
                # Fetch all the rows in a list of lists.
                movies = cursor.fetchall()
            except:
                print("Error: unable to fetch data")
            db.close()
            if movies:
                return render_template("Movies.html",results=movies)
            else:
                return render_template("Movies.html",results=False)
        else:
            return redirect(url_for('movies'))
    return redirect(url_for('index'))


@app.route('/registerForm', methods=['GET', 'POST'])
def registerForm():
    result = request.form
    genre = result.getlist('genre')
    ob = register()#creating object for register class
    ans = ob.registerfunc(*genre, **result)
    email = result['mailId']
    if ans == True:
        status = True
        return render_template("signup.html", status=status)
    else:
        return render_template("signup.html", status=False)


@app.route('/single')
@app.route('/single/<ID>')
def single(ID):
    print(ID)
    if g.mail:
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select * from movies where ID=%s"
        value = (ID)
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            movie = cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        db.close()
        obj=singleMovie()
        genre=obj.getGenre(*movie)
        rating=obj.getrating(g.mail,ID)
        avg=obj.getAvgRating(ID)

        user_id = ""
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select id from users where email=%s"
        value = (g.mail)
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            res = cursor.fetchall()
            user_id = res[0][0]
        except:
            print("Error: unable to fetch data")
        db.close()
        y = homefile()
        results = y.homefunc()
        recommend = y.getrecommend(user_id)
        if recommend == None:
            return render_template("singleMovie.html",movie=movie,genre=genre,id=ID,rating=rating,avg=avg,results1=recommend)

        return render_template("singleMovie.html",movie=movie,genre=genre,id=ID,rating=rating,avg=avg,results1=recommend)

@app.route('/rating',methods=['GET', 'POST'])
def rating():
    if g.mail:
        user_id=""

        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select id from users where email=%s"
        value = (g.mail)
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            movie = cursor.fetchall()
            user_id=movie[0][0]
        except:
            print("Error: unable to fetch data")
        db.close()
        result=request.form
        if "star" in result:
            print(result["star"])
            print(result["movie_id"])
            print("user=",user_id)
            obj=ratingfile
            #status=obj.ratingfunc(user_id,result["movie_id"],result["star"])
            status=obj.ratingfunc(obj,user_id,**result)
            if status==True:
                return redirect(url_for("home"))
        return redirect(url_for("home"))

@app.route('/myprofile', methods=['GET', 'POST'])
def myprofile():
    if g.mail:
        user = session.get("mail")
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
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
    #app.run(debug=False,host="0.0.0.0")
