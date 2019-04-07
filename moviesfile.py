import pymysql
class moviefile():
    def moviesfunc(self):
        db = pymysql.connect("localhost", "root", "lokesh1999", "movieRecommendataion")
        cursor = db.cursor()
        sql = "select ID,poster_url,Movie from movies"
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        db.close()
        return results