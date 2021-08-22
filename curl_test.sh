echo '{"text":"some testing data"}' > test_input.json
curl "http://0.0.0.0:8080/upload" -X POST --header 'Content-Type: application/json' -d @./test_input.json

curl "http://0.0.0.0:8080/download"

curl "http://0.0.0.0:8080/download"
curl "http://0.0.0.0:8080/download"
curl "http://0.0.0.0:8080/download"
curl "http://0.0.0.0:8080/download"

curl "http://0.0.0.0:8080/upload" -X POST --header 'Content-Type: application/json' -d @./test_input01.json

curl "http://0.0.0.0:8080/list"

curl "http://0.0.0.0:8080/download"
curl "http://0.0.0.0:8080/list"

