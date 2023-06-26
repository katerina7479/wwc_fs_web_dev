# Strategy for environment / handling static files

1. We're going to use dotenv for importing all secrets and environment variables
2. We can use the same settings.py file for both cases if we can condition some of the settings
   3. In particular, locally we will use local media and static directories, but remotely we will use S3 buckets
   4. So, we're adding this to our settings.py
    
```python
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# Not handling this at this layer
ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

# ...

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
    'rest_framework',
    'storages',
    'src',
]


# ...

if not DEBUG:  # i.e., if in production
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_MEDIA_BUCKET_NAME = os.getenv('AWS_MEDIA_BUCKET_NAME')

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    MEDIA_URL = f'https://{AWS_MEDIA_BUCKET_NAME}.s3.amazonaws.com/'
else:
    # Local development settings for static files
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
