#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Overall route
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# This makes specific routes for users
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Run a development server diretly through the script
#   Also, the server will automaticall restart when
#   a change is made to app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)