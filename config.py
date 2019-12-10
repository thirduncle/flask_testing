import os

class Config:
    """Set Flask configuration vars."""

    # General Config
    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secter_key'
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')