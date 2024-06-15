from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>This is a Heading</h1>\n<p>Hello, World!</p>"

@app.route("/taige")
def taige():
    return "<h1>Hello Taige!</h1>\n<p>This is another example</p>"

@app.route("/info")
def info():
    return "<h1>Info</h1>\n<p>Information about stuff and things!</p>"
