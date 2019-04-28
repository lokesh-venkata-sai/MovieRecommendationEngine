import unittest
import main
import login
import singleMoviefile

class Testmain(unittest.TestCase):
    def test_validateLogin(self):
        obj=login.login()
        dict={
            "mailId":"exam@gmail.com",
            "password":"exam"
        }
        x=obj.validateLogin(**dict)
        self.assertEqual(x,True)

    def test_getrating(self):
        obj=singleMoviefile.singleMovie()
        x=obj.getrating("exam1@gmail.com",48)
        self.assertEqual(x,5)

    def test_getGenre(self):
        obj=singleMoviefile.singleMovie()
        dict=[1,"https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@..jpg","Toy Story (1995)",	0,	0,	0	,1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,]
        x=obj.getGenre(dict)
        y=" Animation"+" Children"+" Comedy"
        self.assertEqual(x,y)