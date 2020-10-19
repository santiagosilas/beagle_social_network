from flask import Flask

app = Flask(__name__)

# Carrega as configurações a partir de config.py
app.config.from_object('config')

from beagle_social_network import routes

