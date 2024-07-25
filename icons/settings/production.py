import os
from .base import *
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

SECRET_KEY = str(os.getenv('SECRET_KEY'))

ALLOWED_HOSTS = ['icons.bradrice.com']
ALLOWED_HOSTS = [
  'localhost',
  '127.0.0.1',
  '45.56.110.221',
  'icons.bradrice.com']

try:
    from .local import *
except ImportError:
    pass
