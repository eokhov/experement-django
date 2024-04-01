command = '/home/eok/code/sito/env/bin/gunicorn'
pythonpath = 'home/eok/code/sito/sito_site'
bind = '0.0.0.0:8001'
worker = 3
user = 'eok'
limit_request_field = 32000
limit_request_field_size = 0
raq_env = 'DJANGO_SETTINGS_MODULE=sito_site.settings'
