# Django settings for mrben project.

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Calculated site root
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

BASE_URL = 'http://mrben.co.uk'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = BASE_URL + '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'mrben.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.admin',
    'mrben.main',
    'disqus',
    'south',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth', 
    'django.core.context_processors.debug', 
    'django.core.context_processors.i18n', 
    'django.core.context_processors.media', 
    'django.core.context_processors.request',

    'mrben.context_processors.latest_tweets',
    'mrben.context_processors.latest_lastfm_tracks',
    'mrben.context_processors.random_flickr_picture',
    'mrben.context_processors.features',
)

TWEET_LIMIT = 5
TWITTER_USER = ''
TWITTER_CACHE_TIMEOUT = 120
LASTFM_KEY = ''
LASTFM_SECRET = ''
LASTFM_USER = ''
LASTFM_PWDHASH = ''
LASTFM_CACHE_TIMEOUT = 900
FLICKR_KEY = ''
FLICKR_SECRET = ''
FLICKR_ID = ''
FLICKR_CACHE_TIMEOUT = 1800
DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = ''

ENTRIES_PER_PAGE = 4
FEATURE_SIDEBAR_COUNT = 2
FEED_CACHE_TIMEOUT = 1800

CACHE_MIDDLEWARE_SECONDS = 60
CACHE_MIDDLEWARE_KEY_PREFIX = 'mrben'

try:
	from settings_local import *
except ImportError:
	pass