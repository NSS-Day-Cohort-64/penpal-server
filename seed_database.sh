#!/bin/bash

rm db.sqlite3
rm -rf ./penpalapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations penpalapi
python3 manage.py migrate penpalapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata topics
python3 manage.py loaddata letters
python3 manage.py loaddata tags