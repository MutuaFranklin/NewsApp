from flask import Flask, config
from flask_bootstrap import Bootstrap



#Initializing application
app = Flask(__name__,instance_relative_config = True)
app.config.from_pyfile('config.py') 
# app.config.from_object('')



bootstrap = Bootstrap(app)


from app import views
from app import error
