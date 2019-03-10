#!/bin/sh
wget -q0- https:toolbelt.heroku.com/intall-ubuntu.sh | sh
docker login -e _ -u --password=$HEROKU_API_KEY registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME