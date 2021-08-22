import requests
import json
import base64
import pprint
pp = pprint.PrettyPrinter()
with open('/home/p/Downloads/test.gif', 'rb') as f:
    data = f.read()

payload = {
    'text': 'quick fox',
    'image': base64.b64encode(data).decode('utf-8')
}
upload = "http://0.0.0.0:8080/upload"
req = requests.post(upload, data=json.dumps(payload))

list_things = "http://0.0.0.0:8080/list"
req = requests.get(list_things)
huh = json.loads(requests.get(list_things).text)
pp.pprint(huh)
download_thing = "http://0.0.0.0:8080/download"
req = requests.get(download_thing)
pp.pprint(json.loads(req.text))


