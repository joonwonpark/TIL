import requests
from bs4 import BeautifulSoup

# 네이버 금융 - 시장지표 - 원달러 환율 가져오기

url = 'https://finance.naver.com/marketindex/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
us_dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
print(us_dollar)
