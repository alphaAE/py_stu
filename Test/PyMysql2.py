# 首先控制台使用pip安装连接Mysql的包 'pip3 install PyMySQL'
# 导入包
import pymysql as mysql

# 打开数据库连接 ('数据库地址','数据库用户名','密码','数据库名')
db = mysql.connect(host="127.0.0.1",
                   user="stu",
                   password="123456",
                   database="studb")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

## 插入数据
sql = """INSERT INTO people(name, age)
         VALUES ('李华', 22)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except BaseException:
    # 如果发生错误则回滚
    db.rollback()

## 更新数据
sql = "UPDATE people SET age = age + 1 WHERE name = '{}'".format('李华')
try:
    cursor.execute(sql)
    db.commit()
except BaseException:
    db.rollback()

## 查询数据
sql = "SELECT * FROM people WHERE id = {}".format(5)
try:
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # 便利数据集
    for row in results:
        _id = row[0]
        _name = row[1]
        _age = row[2]
        # 打印结果
        print("id={},name={},age={}".format(_id, _name, _age))
except BaseException:
    print("错误：无法获取数据")

## 数据删除
sql = "DELETE FROM people WHERE id != {}".format(5)
try:
    cursor.execute(sql)
    db.commit()
except BaseException:
    db.rollback()

# 关闭数据库连接
db.close()
