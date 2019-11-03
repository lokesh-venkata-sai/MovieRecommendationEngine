import pymysql
mysql_server="mysql_server"

class register():

    def registerfunc(self,*genre,**result):
        self.name=result['username']
        self.mailId= result['mailId']
        self.password=result['password']
        self.confPassword=result['confirmPassword']
        self.genre=genre
        self.Action=0
        self.Adventure=0
        self.Animation=0
        self.Comedy=0
        self.Drama=0
        self.Fantasy=0
        self.Horror=0
        self.Romance=0
        self.Sci_Fi=0
        self.Thriller=0
        #print("genre: ",genre)
        for item in genre:
            if item=="Action":
                self.Action=1
            if item=="Adventure":
                self.Adventure=1
            if item=="Animation":
                self.Animation=1
            if item=="Comedy":
                self.Comedy=1
            if item=="Drama":
                self.Drama=1
            if item=="Fantasy":
                self.Fantasy=1
            if item=="Horror":
                self.Horror=1
            if item=="Romance":
                self.Romance=1
            if item=="Sci-Fi":
                self.Sci_Fi=1
            if item=="Thriller":
                self.Thriller=1

        #print(self.name,self.mailId,self.password,self.Action,self.Adventure,self.Animation,self.Comedy,self.Drama,self.Fantasy,self.Horror,self.Romance,self.Sci_Fi,self.Thriller)
        # Open database connection
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        # prepare a cursor object using cursor() method
        db.autocommit(False)
        cursor = db.cursor()
        # execute SQL query using execute() method.

        sql = "insert into users values(Null,%s,%s,aes_encrypt(%s,'passkey'),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val =(self.name,self.mailId,self.password,int(self.Action),int(self.Adventure),int(self.Animation),int(self.Comedy),int(self.Drama),int(self.Fantasy),int(self.Horror),int(self.Romance),int(self.Sci_Fi),int(self.Thriller))
        try:
            #print("in try")
            # Execute the SQL command
            cursor.execute(sql,val)
            #print("command executed")
            # Fetch all the rows in a list of lists.
        except Exception as e:
            print(e)
            print("Error: unable to insert data")
            db.close()
            return False
        db.commit()
        db.close()
        return True

