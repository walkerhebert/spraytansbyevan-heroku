from flask import Flask, render_template, request, flash, session, redirect

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "Murgow-app-key"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("home.html")


@app.route("/spraytans")
def spraytans():

    
    return render_template("spraytans.html")


@app.route("/about_tans")
def about_tans():
    
    return render_template("about-spraytan.html")

@app.route("/Gallery")
def Gallery():
    
    return render_template("gallery.html")
    
    
@app.route("/care_instructions")
def care_instructions():
    
    return render_template("care-instructions.html")



@app.route("/FAQ")
def FAQ():
    
    return render_template("FAQ.html")

@app.route("/tan_landing")
def tan_landing():
    
    return render_template("tan-landing.html")



if __name__ == "__main__":
    app.run(debug=True)