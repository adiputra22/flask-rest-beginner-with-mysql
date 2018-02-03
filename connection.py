import pymysql.cursors

connection = pymysql.connect(host='localhost',user='root',password='root',unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",db='flask-rest-mysql',port=3306)
