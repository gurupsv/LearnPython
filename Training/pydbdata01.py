import pymysql
db = pymysql.connect("localhost","root","","test" )
#(url,uname,passwd,dbname)
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute("Select * from user")
rows = cursor.fetchall()
print(rows)