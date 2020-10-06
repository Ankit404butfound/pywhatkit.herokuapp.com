from flask import Flask

flaskapp = Flask(__name__)
from app import routes
