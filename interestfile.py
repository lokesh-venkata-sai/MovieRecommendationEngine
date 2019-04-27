import pymysql
mysql_server="localhost"
class update():
    def updatefunc(self,*genre,**result):
        self.username=result['username']
        self.genre=genre
        self.Action = 0
        self.Adventure = 0
        self.Animation = 0
        self.Comedy = 0
        self.Drama = 0
        self.Fantasy = 0
        self.Horror = 0
        self.Romance = 0
        self.Sci_Fi = 0
        self.Thriller = 0

        for item in self.genre:
            if item == "Action":
                self.Action = 1
            if item == "Adventure":
                self.Adventure = 1
            if item == "Animation":
                self.Animation = 1
            if item == "Comedy":
                self.Comedy = 1
            if item == "Drama":
                self.Drama = 1
            if item == "Fantasy":
                self.Fantasy = 1
            if item == "Horror":
                self.Horror = 1
            if item == "Romance":
                self.Romance = 1
            if item == "Sci-Fi":
                self.Sci_Fi = 1
            if item == "Thriller":
                self.Thriller = 1
        db = pymysql.connect(mysql_server, "root", "lokesh1999", "movieRecommendation")
        db.autocommit(False)
        cursor = db.cursor()
        sql = "update users set Action=%s,Adventure=%s,Animation=%s,Comedy=%s,Drama=%s,Fantasy=%s,Horror=%s,Romance=%s,Sci_Fi=%s,Thriller=%s where username=%s"
        #for item in self.genre:

        val=(int(self.Action),int(self.Adventure),int(self.Animation),int(self.Comedy),int(self.Drama),int(self.Fantasy),int(self.Horror),int(self.Romance),int(self.Sci_Fi),int(self.Thriller),self.username)
        try:
            cursor.execute(sql, val)
        except Exception as e:
            print("Error: unable to insert data")
            print(e)
            db.close()
            save = False
            return save
        db.commit()
        db.close()
        return True
