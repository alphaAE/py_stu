
import pymysql as mysql

db = mysql.connect(host="db.alphaae.com", user="stu", password="123456", database="studb")

cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# date = cursor.fetchone()
# print("DB version: {}".format(date))

for i in range(10):
    cursor.execute("INSERT INTO student(`name`,sex) VALUES ('李华{}', '1'),('梨花{}', '0')".format(i, i))
    db.commit()
    print("Data: {}".format(i))

db.close()
