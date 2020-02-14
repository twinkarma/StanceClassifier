#!/bin/bash
# Script for starting the gunicorn host on the server
export LANG=en_GB.UTF-8
source /home/twin/miniconda3/bin/activate rumours
exec gunicorn  --timeout 300 --bind 0.0.0.0:9125 wsgi
