import os
from flask import Flask
from SPIE_table import *


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("postgres://nvlfoaeohtattz:df9dc3553f6eeee149be12c")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	db.create_all()

if __name__=="__main__":
	with app.app_context():
		main()