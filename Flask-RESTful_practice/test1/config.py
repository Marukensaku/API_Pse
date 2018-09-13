


class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class MySQLConfig:
    MYSQL_USERNAME = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_HOST = '172.16.2.148'


class DevelopmentConfig(Config):
    DEBUG = True
    database = 'mysql_dev'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(MySQLConfig.MYSQL_USERNAME,
                                                                   MySQLConfig.MYSQL_PASSWORD,
                                                                   MySQLConfig.MYSQL_HOST, database)


class TestingConfig(Config):
    TESTING = True
    database = 'mysql_test'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(MySQLConfig.MYSQL_USERNAME,
                                                                   MySQLConfig.MYSQL_PASSWORD,
                                                                   MySQLConfig.MYSQL_HOST, database)


class ProductionConfig(Config):
    database = 'mysql_product'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(MySQLConfig.MYSQL_USERNAME,
                                                                   MySQLConfig.MYSQL_PASSWORD,
                                                                   MySQLConfig.MYSQL_HOST, database)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
