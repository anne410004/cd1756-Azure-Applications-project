import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'articlecmsstorage2'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'placeholder'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'article-cms-server2.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'article-cms-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'placeholder'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'placeholder'
    AUTHORITY = "https://login.microsoftonline.com/87e60dd5-c8b5-488a-bcc4-75d6aaed2ba8"
    CLIENT_ID = "7388d66f-0ce2-49b6-8b2a-0bb6a1934d24"

    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"