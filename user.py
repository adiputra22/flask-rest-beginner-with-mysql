import pymysql.cursors
from flask_restful import Resource, reqparse

class User:

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = pymysql.connect(host='localhost',user='root',password='root',unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",db='flask-rest-mysql',port=3306)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))
        row = cursor.fetchone()

        if(row):
            user = cls(*row)
        else:
            user = None

        connection.close()

        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = pymysql.connect(host='localhost',user='root',password='root',unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",db='flask-rest-mysql',port=3306)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=%s"
        cursor.execute(query, (_id,))
        row = cursor.fetchone()

        if(row):
            user = cls(*row)
        else:
            user = None

        connection.close()

        return user

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']) :
            return {"message": "A user with that username already exists"}, 400

        connection = pymysql.connect(host='localhost',user='root',password='root',unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",db='flask-rest-mysql',port=3306)
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, %s, %s)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {
            "message": "User created successfully."
        }, 201
