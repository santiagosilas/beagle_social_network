from flask import Flask

app = Flask(__name__)

from beagle_social_network import routes

