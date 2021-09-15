import requests
r = requests.get('http://a9e0-35-193-131-231.ngrok.io:80/temp')
#print(r.status_code, r.headers, r.encoding)
print(r.text)
