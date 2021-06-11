from config.defalult import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xdd\x01\x1c\x1c\xb0V\x0c\x10\xc0>M\xa1+\xd64\x9e'