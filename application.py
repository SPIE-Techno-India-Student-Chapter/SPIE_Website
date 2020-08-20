from flask import Flask, render_template, session, request
from table import *
import config

application=app=Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(application)

#def store_into_SPIE_table(session):
#	data = Candidates(name = name, email = email, post = post,
 #   organisation = organisation, ph_number = ph_number)

@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/registration")
def register():
    return render_template("registration.html")


@app.route("/thanks",methods=["POST"])
def submit():
    name=session["name"] = request.form.get("Name")
    organisation=session["organisation"]= request.form.get("organisation")
    email=session["email"]= request.form.get("email")
    ph_number= session["ph_number"] = str(request.form.get("ph_number"))
    post=session["post"] = request.form.get("role")
    data = Registrant(name = name, email = email, post = post, organisation = organisation, ph_number = ph_number)
    db.session.add(data)
    db.session.commit()
    return render_template("thanks.html")



if __name__=="__main__":
    app.run(host = '0.0.0.0',port = 8080)



