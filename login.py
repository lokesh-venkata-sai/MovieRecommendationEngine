from flask_wtf import Form
import pymysql
class login():
    def validateLogin(self,**data):
            self.mailId = data['mailId']
            self.password = data['password']

            # Open database connection
            db = pymysql.connect("localhost", "root", "lokesh1999", "movieRecommendataion")
            # prepare a cursor object using cursor() method
            db.autocommit(False)
            cursor = db.cursor()
            # execute SQL query using execute() method.

            #sql = "SELECT cast(aes_decrypt(%s,'passkey') as char(50)) as password FROM users where mailId=%s "
            val= (self.password,self.mailId)
            # cursor.execute("SELECT VERSION()")
            # Fetch a single row using fetchone() method.
            try:

                # Execute the SQL command
                cursor.execute("SELECT cast(aes_decrypt(password,'passkey') as char(50)) from users where email=%s",(self.mailId))

                # Fetch all the rows in a list of lists.
                results = cursor.fetchall()
                password=results[0][0]
                db.commit()
                db.close()
                if password==self.password:

                    return True
                else:
                    return False
            except:
                print("Error: unable to fetch data")
                db.commit()
                db.close()
                return False
            # disconnect from server
