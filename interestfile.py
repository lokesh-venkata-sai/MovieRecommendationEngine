import pymysql
class interest():
    def interestfunc(self,user,result):
        self.user=user
        self.genre=result
        db = pymysql.connect("localhost", "root", "lokesh1999", "movieRecommendataion")
        db.autocommit(False)
        cursor = db.cursor()
        sql = "insert into interests values(%s,%s)"
        #for item in self.genre:
        print("item: ",self.genre)
        val=(user,self.genre)
        try:
            cursor.execute(sql, val)
        except:
            print("Error: unable to insert data")
            db.commit()
            db.close()
            save = False
            return save
        db.commit()
        db.close()
        return True
