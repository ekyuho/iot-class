import requests 
URL = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1141058500'

r = requests.get(URL) 
print('stat code=', r.status_code )
print(r.text)

'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
t = soup.find_all("temp")
temp=[]
for i in t:
  print(i)
  temp.append(str(i).replace('<temp>','').replace('</temp>',''))
'''
'''
import matplotlib.pyplot as plt
import numpy as np
plt.plot(temp)
'''
