from flask import Flask, render_template
from VIC import *
from modul_stepkos import *

app = Flask(__name__)

app.debug = True


@app.route("/encrypt_file")
def encrypt():
    pass

@app.route("/")
def index():
    return render_template("index.html")
 
if __name__ == "__main__":
    app.run()
