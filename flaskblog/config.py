import os

class Config:
	
	SECRET_KEY = os.environ.get('SECRET_KEY')
##a way to generate this(after v3.6):
##import secrets
##secrets.token_hex(length)
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
##'sqlite:///site.db'
##/// means relative path(./)
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 465
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.environ.get('DB_MAIL')
	MAIL_PASSWORD = os.environ.get('DB_MAIL_PASSWORD')
	MAIL_DEFAULT_SENDER = os.environ.get('DB_MAIL')

