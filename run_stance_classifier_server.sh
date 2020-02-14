#!/bin/bash
# Script for starting the gunicorn host on the server

source /home/twin/miniconda3/bin/activate rumours
exec gunicorn  --timeout 300 --bind 0.0.0.0:9125 wsgi