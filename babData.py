import requests
from bs4 import BeautifulSoup
 
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://mportal.cau.ac.kr/main.do',headers=headers)
 
soup = BeautifulSoup(data.text, 'html.parser')
s = soup.select('#carteP005 > li > dl > dd > label > div')
f = open("./새파일.txt", 'w')
f.write(str(soup))
f.close()
print(soup)
