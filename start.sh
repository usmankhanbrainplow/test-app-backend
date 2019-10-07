#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn Tester.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
