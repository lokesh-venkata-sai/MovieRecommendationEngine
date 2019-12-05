import pymysql
#mysql_server="mysql_server"
mysql_server="localhost"

class homefile():
    def homefunc(self):
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select ID,poster_url,Movie from movies LIMIT 18"
        results=""
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        db.close()
        #print(type(results))
        return results

    def getrecommend(self,user_id):
        results1=""
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select movieId from recommend where userId=%s"
        val=(int(user_id))
        try:
            # Execute the SQL command
            cursor.execute(sql,val)
            # Fetch all the rows in a list of lists.
            results1 = cursor.fetchall()
        except:
            print("Error: unable to fetch data1")


        #print(results1)
        res = tuple();

        for i in results1:
            results2=tuple()
            sql = "select ID,poster_url,Movie from movies where ID=%s"
            val=(int(i[0]))
            try:
                # Execute the SQL command
                cursor.execute(sql,val)
                # Fetch all the rows in a list of lists.
                results2 = cursor.fetchall()
            except:
                print("Error: unable to fetch data2")
            res=res+results2

        db.close()
        return res