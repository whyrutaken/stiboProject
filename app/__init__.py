from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import SECRET_KEY

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)

from app import routes
