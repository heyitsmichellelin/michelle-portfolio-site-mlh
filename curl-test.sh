curl --request POST http://localhost:5000/api/timeline_post -d 'name=Ian&email=dummyEmail@gmail.com&content=Just Added to my database!'

EMAIL=$(curl --request GET http://localhost:5000/api/timeline_post | jq -r '.timeline_posts | first | .email')

if [ $EMAIL == "dummyEmail@gmail.com" ]; then
    echo "Test Passed"
else
    echo "Test Failed"    
fi
