import os

class Config(object):

    SECRET_KEY = 'aplikasipmb'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/pmb'
    SQLALCHEMY_TRACK_MODIFICATION = False