import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '9035326400',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())