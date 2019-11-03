import pymysql
mysql_server="mysql_server"

class moviefile():
    def moviesfunc(self):
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        cursor = db.cursor()
        sql = "select ID,poster_url,Movie from movies"
        results=""
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        db.close()
        return results