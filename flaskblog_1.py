from flask import Flask
app = Flask(__name__)

# homepage -- "/" or "/home"
@app.route("/")
@app.route('/home')
def hello():
    return "<h1> Hello Cyborgs!! </h1>"

# when added /about to the link return this
@app.route("/about")
def about():
    return "This page is about python programming"

# when run from the file __name__ will be __main__ 
# this allows us to run python flaskblog.py instead of flask run flaskblog.py
if __name__ == '__main__':
    app.run(debug=True)