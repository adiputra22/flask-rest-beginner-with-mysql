import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='flask-rest-mysql',
    port=3306
)
