from flask import Flask
import json

app = Flask(__name__)

@app.route("/simple_string")
def return_a_simple_string():
    return "this is a simple string returned"

app.run(host = "0.0.0.0")
    