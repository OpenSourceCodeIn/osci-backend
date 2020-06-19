from flask import Flask, request
from flask_restful import Resource, Api
import random

from . import db

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def post(self, username):
        db.add_student(username, request.form['name'], request.form['email'], request.form['password'], str(random.randint(0, 1000000000)))
        return None, 204

api.add_resource(Student, '/student/<string:username>')
if __name__ == '__main__':
    app.run(debug=True)
