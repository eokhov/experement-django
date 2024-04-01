#!/bin/bash
source /home/eok/code/sito/env/bin/activate
cd ./sito_site/ && exec gunicorn -c "/home/eok/code/sito/sito_site/gunicorn_config.py" sito_site.wsgi
