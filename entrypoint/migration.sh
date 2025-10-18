#!/bin/bash
# set -o errexit
# set -o pipefail
# set -o nounset

python manage.py createcachetable && python manage.py makemigrations --merge && python manage.py migrate && exec "$@"
