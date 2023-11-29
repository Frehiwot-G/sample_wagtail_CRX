#!/bin/sh

if [ -z ${ENVIRONMENT} ]; then export ENVIRONMENT=local; fi

# build static assets
python /usr/src/sample_wagtail_CRX/sample_website/manage.py collectstatic --noinput

# start api with gunicorn
/usr/src/sample_wagtail_CRX/sample_website/virtualenv/bin/gunicorn sample_website.wsgi -b 0.0.0.0:8000 --chdir=/usr/src/sample_wagtail_CRX/sample_website
