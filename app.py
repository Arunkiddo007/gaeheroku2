from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello():
    return "<h1>Hello Arunraj</h1>"

if _name_ == '_main_':
    app.run(port=5000, threaded=True)
