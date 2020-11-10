
import pymysql as mysql

db = mysql.connect("db.alphaae.com", "testuser", "123456", "TESTDB")

cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# date = cursor.fetchone()
# print("DB version: {}".format(date))

for i in range(1000000):
    cursor.execute("INSERT INTO student(`name`,sex) VALUES ('李华{}', '1'),('梨花{}', '0')".format(i, i))
    db.commit()
    print("Data: {}".format(i))

db.close()
