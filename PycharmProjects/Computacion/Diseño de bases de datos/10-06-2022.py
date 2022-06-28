import pymysql
db = pymysql.connect(host="127.0.0.1", user= "root", passwd="43664152a", db="sakila")
cursor = db.cursor()
cursor.execute("SELECT count(*) from STAFF")
data = cursor.fetchone()
print("Nro de registros en Staff: %s" % data)
db.close()