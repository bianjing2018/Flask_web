import datetime

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:bianjing@49.234.19.31:3306/ShadowsocksX?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = True
REMEMBER_COOKIE_DURATION = datetime.timedelta(hours=1)