from flask import Flask
from flask import request
app = Flask(__name__)
app.run(threaded=True, port=5000)
@app.route('/')
def hello_world():
    return 'Hello from Flask!'
