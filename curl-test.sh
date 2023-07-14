#!/bin/bash

before=$(curl --request GET http://localhost:5000/api/timeline_post) | jq length
status_code=$(curl --write-out %{http_code} --silent --output /dev/null -X POST http://localhost:5000/api/timeline_post -d 'name=Maxx&email=maxx@gmail.com&content=it is summertime'
)
if [[ "$status_code" -eq 200 ]] ; then
    after=$(curl --request GET http://localhost:5000/api/timeline_post | jq length)
    if [ $after -gt $before ] ; then
        echo "Successfully added data"
    else
        echo "Unable to add data"
    fi
fi