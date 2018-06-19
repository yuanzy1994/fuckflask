#/usr/bin/python

class Config(object):
    pass

class ProdConfig(object):
    pass

class DevConfig(object):
    debug = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:redhat@118.25.68.122:3306/flask"
