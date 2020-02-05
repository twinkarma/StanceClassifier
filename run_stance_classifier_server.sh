#!/bin/bash
# Script for starting the gunicorn host on the server

source /home/twin/miniconda3/bin/activate rumours
exec python flask_server.py
