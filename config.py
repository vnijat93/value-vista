import os
from os import path

basedir = path.abspath(path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "CSE682"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "data.sqlite")


config = {"dev": DevelopmentConfig, "default": DevelopmentConfig}
