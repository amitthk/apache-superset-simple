#!/bin/bash
set -e

export FLASK_APP=superset

superset db upgrade 

superset fab create-admin --username admin --firstname Admin --lastname User --email admin@superset.com --password admin

superset init

# To start a development web server on port 8088
superset run -p 8088 --host 0.0.0.0 --with-threads --reload --debugger