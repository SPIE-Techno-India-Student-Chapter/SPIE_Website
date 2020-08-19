from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registrant(db.Model):
	__tablename__ = "participants"
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String, nullable=False)
	organisation = db.Column(db.String, nullable=False)
	post = db.Column(db.String, nullable=False)
	ph_number = db.Column(db.Integer, nullable=False)
	email = db.Column(db.String, nullable=False)