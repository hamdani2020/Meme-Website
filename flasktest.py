from flask import Flask
app=Flask(__name__)


@app.route("/")

def index():
    return "I love lusitech IT Consult"



app.run(host="0.0.0.0", port=5001)
