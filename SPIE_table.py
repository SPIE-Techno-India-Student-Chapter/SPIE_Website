from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registrant(db.Model):
	__tablename__ = "Details"
	id = db.column(db.Integer, primary_key=True)
	name = db.column(db.String, nullable=False)
	organisation = db.column(db.String, nullable=False)
	post = db.column(db.String, nullable=False)
	ph_number = db.column(db.Integer, nullable=False)
	email = db.column(db.Integer, nullable=False)
