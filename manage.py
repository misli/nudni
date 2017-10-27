#!/bin/bash

if ! which django-cms &> /dev/null; then
    if ! test -e env/bin/activate; then
        virtualenv env
    fi
    . env/bin/activate
    if ! which django-cms &> /dev/null; then
        pip install -r requirements.txt
    fi
fi

export PYTHONPATH=.
export DEBUG=TEMPLATE
export SITE_MODULE=nudni
exec django-cms "$@"
