import pymysql
mysql_server="mysql_server"
class ratingfile:
    def ratingfunc(self,user_id,**result):
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "insert into ratings values(%s,%s,%s)"
        #val=(int(user_id),int(movie_id),int(rating))
        val=(int(user_id),int(result["movie_id"]),int(result["star"]))
        try:
            # Execute the SQL command
            cursor.execute(sql,val)
        except:
            print("Error: unable to insert data")
            db.commit()
            db.close()
            return False
        print("inserted")
        db.commit()
        db.close()
        return True