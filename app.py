import os
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	email = db.Column(db.Text)
	username = db.Column(db.Text)

	def __init__(self, name, email, username):
		self.name = name
		self.email = email
		self.username = username
		
db.create_all()

@app.route('/')
def index():
	return "For the demo, navigate to the endpoint /"

@app.route('/signup')
def signup():
	name = request.args.get('name')
	email = request.args.get('email')
	username = request.args.get('username')
	new_user = User(name, email, username)
	db.session.add(new_user)
	return name + " was successfully added to the database!"

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
