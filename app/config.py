import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///manergy.db'
    SECRET_KEY = os.environ.get('SECRET_KEY', '28d6afc0c91566bbefae52ba')
    YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
    ADMIN_LIST = [value for key, value in os.environ.items()
                  if key.endswith('ADMIN')]
    
    def init_app(self, app):
        pass
