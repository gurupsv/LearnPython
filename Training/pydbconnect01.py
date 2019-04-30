import pymysql
db = pymysql.connect("localhost","root","","test" )
#(url,uname,passwd,dbname)
cursor = db.cursor()
cursor.execute("""CREATE TABLE USER (
         FNAME  CHAR(20) NOT NULL,
         LNAME  CHAR(20))""")
db.close()