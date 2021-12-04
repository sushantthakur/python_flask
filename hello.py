from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sushant")
def hello_world1():
    return "<p>Hello, Im Sushant</p>"
    if not TRUE:
        pass

        
