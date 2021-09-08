import requests
r = requests.get('http://www.google.com')
print(r.status_code, r.headers, r.encoding)
print(r.text)
