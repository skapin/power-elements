import os


SETTINGS = {}
# settings['PROXY_IP'] = os.environ['PROXY_IP']
SETTINGS['POSTGRES_HOST'] = os.environ['POSTGRES_HOST']
SETTINGS['POSTGRES_PORT'] = os.environ['POSTGRES_PORT']

SETTINGS['POSTGRES_USER'] = os.environ['POSTGRES_USER']
SETTINGS['POSTGRES_PASSWORD'] = os.environ['POSTGRES_PASSWORD']
SETTINGS['POSTGRES_DB'] = os.environ['POSTGRES_DB']
SETTINGS['DEBUG_MODE'] = bool(os.environ['DEBUG_MODE'])
SETTINGS['QUESTIONS_FILE'] = 'ressources/questions.csv'

# SETTINGS['SAGE_URL'] = 'http://192.168.0.247:9020'
# SETTINGS['SENTRY_DSN'] = 'https://32bb8bab065741b3a4ced72df5ac84c3@sentry.aiotools.ovh/2'
