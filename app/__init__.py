import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager

mail = Mail()
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view='loginmhs'
login.login_message_category = "danger"
login.login_message = u"Km belum login woe"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] =  True
app.config['MAIL_USERNAME'] = 'pmb.officialtic@gmail.com'
app.config['MAIL_PASSWORD'] = 'Pmbadmin123'

mail.init_app(app)

from app.models import models
from app.routes import routes

