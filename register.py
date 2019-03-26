import pymysql


class register():
    def registerfunc(self, **result):
        self.username = result['username']
        self.mailId = result['mailId']
        self.password = result['password']
        self.confpPassword = result['confirmPassword']

        # Open database connection
        db = pymysql.connect("localhost", "root", "lokesh1999", "movieRecommendataion")
        # prepare a cursor object using cursor() method
        db.autocommit(False)
        cursor = db.cursor()
        # execute SQL query using execute() method.

        sql = "insert into users values(Null,%s,%s,aes_encrypt(%s,'passkey'))"
        val = (self.username, self.mailId, self.password)
        # cursor.execute("SELECT VERSION()")
        # Fetch a single row using fetchone() method.
        try:

            # Execute the SQL command
            cursor.execute(sql, val)
            print("command executed")
            # Fetch all the rows in a list of lists.
            db.commit()
            db.close()
            return True
        except:
            print("Error: unable to fetch data")
            db.commit()
            db.close()
            return False
        return True
