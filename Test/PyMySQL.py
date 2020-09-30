
import pymysql as mysql

db = mysql.connect("db.alphaae.com", "testuser", "123456", "TESTDB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

date = cursor.fetchone()

print("DB version: {}".format(date))

db.close()