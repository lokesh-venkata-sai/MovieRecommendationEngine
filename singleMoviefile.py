import pymysql
#mysql_server="mysql_server"
mysql_server="localhost"

class singleMovie():
    def getGenre(self,*movie):
        genre=""
        if movie[0][4]==1:
            genre+=" Action"
        if movie[0][5] == 1:
            genre += " Adventure"
        if movie[0][6]==1:
            genre+=" Animation"
        if movie[0][7]==1:
            genre+=" Children"
        if movie[0][8]==1:
            genre+=" Comedy"
        if movie[0][9]==1:
            genre+=" Crime"
        if movie[0][10]==1:
            genre+=" Documentary"
        if movie[0][11]==1:
            genre+=" Drama"
        if movie[0][12]==1:
            genre+=" Fantasy"
        if movie[0][13]==1:
            genre+=" Film_Noir"
        if movie[0][14]==1:
            genre+=" Horror"
        if movie[0][15]==1:
            genre+=" Musical"
        if movie[0][16]==1:
            genre+=" Mystery"
        if movie[0][17]==1:
            genre+=" Romance"
        if movie[0][18]==1:
            genre+=" Sci_Fi"
        if movie[0][19]==1:
            genre+=" Thriller"
        if movie[0][20]==1:
            genre+=" War"
        if movie[0][21]==1:
            genre+=" Western"
        return genre

    def getrating(self,mail,movie_id):
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select id from users where email=%s"
        value = (mail)
        user_id=""
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            movie = cursor.fetchall()
            user_id = movie[0][0]
        except:
            print("Error: unable to fetch data")
        db.close()
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select rating from ratings where userID=%s && movieId=%s"
        value = (user_id,movie_id)
        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            movie = cursor.fetchall()
        except:
            print("Error: unable to fetch data")
            db.close()
            return False
        db.close()
        if movie:
            return movie[0][0]
        else:
            return "Not Yet Rated"

    def getAvgRating(self,movie_id):
        avg=""
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select avg(rating) from ratings where movieId = %s"
        value = (int(movie_id))

        try:
            # Execute the SQL command
            cursor.execute(sql, value)
            # Fetch all the rows in a list of lists.
            res = cursor.fetchall()
            avg = res[0][0]
        except:
            print("Error: unable to fetch data")
        db.close()
        return avg
