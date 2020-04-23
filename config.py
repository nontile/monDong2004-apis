#
#


class Config:
    APP_NAME = 'management'
    MAX_IMAGE_SIZE = 5242880  # 5MB


class LocalConfig(Config):
    DEBUG = True
    FLASK_DEBUG = True

    # mysql infomation
    DB = {
        'user': 'dong',
        'password': '1111',
        'host': 'localhost',
        'port': 3306,
        'database': 'pjman'
    }

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_DEBUG = True
    TESTING = True

    DB = {
        'user': 'dong',
        'password': '1111',
        'host': 'localhost',
        'port': 3306,
        'database': 'pjman'
    }

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    FLASK_DEBUG = False

    DB = {
        'user': 'dong',
        'password': '1111',
        'host': 'localhost',
        'port': 3306,
        'database': 'pjman'
    }

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class CIConfig:
    SERVICE = 'travis-ci'
    HOOK_URL = 'web-hooking-url-from-ci-service'
