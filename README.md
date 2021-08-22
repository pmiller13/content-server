# The Content Server -___-

Not really a content server. More like a basic FIFO queue with strict input requirements.

# Supported Operations
* Upload json blob containing (required) text and (optional) base64 encoded image data to queue
* List current data in the queue
* Download/pop next json blob from queue
# Running the server
```
pip install -r requirements.txt
python app.py
```
# Interacting with the server
Upload, list, and download a text entry
```
# Create test json data
echo '{"text":"some testing data"}' > test_input.json

# Upload to content server
curl "http://0.0.0.0:8080/upload" -X POST --header 'Content-Type: application/json' -d @./test_input.json

# List items in content server
curl "http://0.0.0.0:8080/list"

# Download the data
curl "http://0.0.0.0:8080/download"
```
Upload, list, and download a text and image entry
```
curl https://i.imgur.com/s0Fu8yP.jpeg -o test.jpg

base64 test.jpg | tr -d '\n' > test.b64enc

b64=$(cat test.b64enc)

cat << EOF > test_input_with_image.json
{"text":"somewhat of a test","image":"$b64"}
EOF

curl -v "http://0.0.0.0:8080/upload" -X POST -H 'Content-type: application/json' -d @./test_input_with_image.json

curl "http://0.0.0.0:8080/list"
```
# Todo
1) TLS
2) Docker image
3) Auth
