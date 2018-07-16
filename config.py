import os

class Config(object):
    SECRET_KEY = os.environ.get['SECRET_KEY'] or 'aplikasipmb'
    SQLALCHEMY_DATABASE_URI = os.environ.get['DATABASE_URL']  or 'mysql+pymysql://root:@localhost/pmb'
    SQLALCHEMY_TRACK_MODIFICATION = False