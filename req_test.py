import requests as req

responce = req.get('http://google.com')

print(responce.ok)
print(responce.text)