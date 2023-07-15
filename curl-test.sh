#!/bin/bash

# Define the API endpoint URLs
POST_ENDPOINT="http://localhost:5000/api/timeline_post"
GET_ENDPOINT="http://localhost:5000/api/timeline_post"

# Generate a random timeline post data
RANDOM_POST=$(openssl rand -base64 12)

# Send a POST request to create a new timeline post
POST_RESPONSE=$(curl -X POST -H "Content-Type: application/json" -d "{\"post\": \"$RANDOM_POST\"}" $POST_ENDPOINT)

# Check if the POST request was successful
if [[ $POST_RESPONSE =~ "success" ]]; then
  echo "Timeline post created successfully: $RANDOM_POST"
else
  echo "Failed to create timeline post"
  exit 1
fi

# Send a GET request to retrieve the timeline posts
GET_RESPONSE=$(curl -s $GET_ENDPOINT)

# Check if the GET request was successful
if [[ $GET_RESPONSE =~ $RANDOM_POST ]]; then
  echo "Timeline post retrieved successfully"
else
  echo "Failed to retrieve timeline post"
  exit 1
fi
