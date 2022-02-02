import requests

res = requests.get('https://boisecodeworks.com')
if res.status_code == 200:
  print(res.text)
else:
  print('Request Failed')
