import requests 
URL = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1141058500'

r = requests.get(URL) 
print('stat code=', r.status_code )
print(r.text)
