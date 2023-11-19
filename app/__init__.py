from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import CSRF_SECRET_KEY
from openai import OpenAI

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = CSRF_SECRET_KEY
csrf.init_app(app)
openai_client = OpenAI()

from app import routes
