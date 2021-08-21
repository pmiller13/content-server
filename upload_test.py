import requests
import json
import base64

with open('/home/p/Downloads/rr.gif', 'rb') as f:
    data = f.read()

payload = {
    'text': 'quick fox',
    'image': base64.b64encode(data).decode('utf-8')
}

url = "http://0.0.0.0:8080/upload"
req = requests.post(url, data=json.dumps(payload))
print(req.text)
