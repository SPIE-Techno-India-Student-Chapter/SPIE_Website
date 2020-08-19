from flask import Flask, render_template, url_for

app=Flask(__name__)

def store_into_SPIE_table(session):
	data = Candidates(name = name, email = email, post = post,
    organisation = organisation, ph_number = ph_number)

@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/registration")
def register():
    return render_template("registration.html")


@app.route("/registration")
def register():
    return render_template("registration.html")


if __name__=="__main__":
    app.run(debug=True)



