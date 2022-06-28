"""import pymysql

Host = "127.0.0.1"
User = "root"
Password = "43664152a"

database = "integrador"

conn = pymysql.connect(host=Host, user=User, password=Password, db=database)

cur = conn.cursor()

PRODUCT_ID = '1201'
price = 10000
PRODUCT_TYPE = 'PRI'

query = f"INSERT INTO productos(idProductos, nombre, tipo) VALUES('{PRODUCT_ID}', '{price}', '{PRODUCT_TYPE}')"

cur.execute(query)
print(f"{cur.rowcount} details inserted")
conn.commit()
conn.close()"""
import time
print(time.strftime("%d/%m/%y"))