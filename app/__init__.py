from flask import Flask

app = Flask(__name__)
app.debug = True
app.config['BOOTSTRAP_FONTAWESOME'] = True

from app import models, views