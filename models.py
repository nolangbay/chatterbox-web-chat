from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#user chat account
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String, unique=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.username

class chatRoom(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roomName = db.Column(db.String, unique=True)
	userCreated = db.Column(db.Text, nullable=False)

	def __init__(self, roomName, userCreated):
		self.roomName = roomName
		self.userCreated = userCreated
	def __repr__(self):
		return '<Chatroom: {}>'.format(self.roomName)

class messageLog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userSent = db.Column(db.String, nullable=False)
	roomName = db.Column(db.String, nullable=False)
	message = db.Column(db.Text, nullable=False)

	def __init__(self, userName, roomName, message):
		self.userSent = userName
		self.roomName = roomName
		self.message = message

	def __repr__(self):
		return '<Message: {}>'.format(self.message)
