# Django settings for dmt project.
import os.path
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dmt',
        'HOST': '',
        'PORT': 5432,
        'USER': '',
        'PASSWORD': '',
    }
}

if 'test' in sys.argv or 'jenkins' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
            'HOST': '',
            'PORT': '',
            'USER': '',
            'PASSWORD': '',
        }
    }
    CELERY_ALWAYS_EAGER = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SOUTH_TESTS_MIGRATE = False

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=dmt',
]

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
)
PROJECT_APPS = [
    'dmt.api',
    'dmt.main',
    'dmt.claim',
    'dmt.report',
]

ALLOWED_HOSTS = ['localhost', '.ccnmtl.columbia.edu']

USE_TZ = True
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
MEDIA_ROOT = "/var/www/dmt/uploads/"
MEDIA_URL = '/uploads/'
SECRET_KEY = ')ng#)ef_u@_^zvvu@dxm7ql-yb^_!a6%v3v^j3b(mp+)l+5%@h'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'stagingcontext.staging_processor',
    'gacontext.ga_processor',
    'djangowind.context.context_processor',
    'django.core.context_processors.static',
)

MIDDLEWARE_CLASSES = [
    'django_statsd.middleware.GraphiteRequestTimingMiddleware',
    'django_statsd.middleware.GraphiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'waffle.middleware.WaffleMiddleware',
]

ROOT_URLCONF = 'dmt.urls'

TEMPLATE_DIRS = (
    "/var/www/dmt/templates/",
    os.path.join(os.path.dirname(__file__), "templates"),
)

import djcelery
djcelery.setup_loader()

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'compressor',
    'django_nose',
    'django_statsd',
    'bootstrapform',
    'debug_toolbar',
    'waffle',
    'django_jenkins',
    'smoketest',
    'django_extensions',
    'impersonate',
    'interval',
    'dmt.main',
    'dmt.claim',
    'dmt.report',
    'dmt.api',
    'rest_framework',
    'taggit',
    'taggit_templatetags',
    'djcelery',
    'django_markwhat',
]

if 'jenkins' in sys.argv:
    COMPRESS_ENABLED = False

INTERNAL_IPS = ('127.0.0.1', )
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
)

STATSD_CLIENT = 'statsd.client'
STATSD_PREFIX = 'dmt'
STATSD_HOST = '127.0.0.1'
STATSD_PORT = 8125

STATSD_PATCHES = []

BROKER_URL = "amqp://localhost:5672//dmt"
CELERYD_CONCURRENCY = 2

THUMBNAIL_SUBDIR = "thumbs"
EMAIL_SUBJECT_PREFIX = "[dmt] "
EMAIL_HOST = 'localhost'
SERVER_EMAIL = "dmt@ccnmtl.columbia.edu"
DEFAULT_FROM_EMAIL = SERVER_EMAIL

STATIC_URL = "/media/"
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../media/")),
)
STATIC_ROOT = ""
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_URL = "/media/"
COMPRESS_ROOT = "media/"

# WIND settings

AUTHENTICATION_BACKENDS = ('djangowind.auth.WindAuthBackend',
                           'django.contrib.auth.backends.ModelBackend', )
WIND_BASE = "https://wind.columbia.edu/"
WIND_SERVICE = "cnmtl_full_np"
WIND_PROFILE_HANDLERS = ['djangowind.auth.CDAPProfileHandler']
WIND_AFFIL_HANDLERS = ['djangowind.auth.AffilGroupMapper',
                       'djangowind.auth.StaffMapper',
                       'djangowind.auth.SuperuserMapper']
WIND_STAFF_MAPPER_GROUPS = ['tlc.cunix.local:columbia.edu']
WIND_SUPERUSER_MAPPER_GROUPS = ['anp8', 'jb2410', 'zm4', 'egr2107',
                                'sld2131', 'amm8', 'mar227', 'jed2161']

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True
LOGIN_REDIRECT_URL = "/"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS':
    'rest_framework.serializers.HyperlinkedModelSerializer',

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
