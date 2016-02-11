import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = " l\x96\xb0\xe7\xfe\x8dRa\xad`\x13\x9ci|\x16\x9fG\xcc\xe0\t-\xaf\xa4"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False