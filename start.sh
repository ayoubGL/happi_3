#!/bin/bash

# Start Gunicorn process
echo starting Gunicorn.
exec gunicorn happ_3.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
