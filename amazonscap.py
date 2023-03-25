from flask import Flask
#from bs4 import Beautifulsoup 
from bs4 import BeautifulSoup
import requests
 
app= Flask(__name__)

@app.route("/")
def scrap():
  url = 'https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD/ref=sr_1_1_sspa?crid=3PDOMMF56451M&keywords=iphone&qid=1679652171&sprefix=iphone%2Caps%2C207&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
  Headers=({"user-agents":"https://explore.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes", "Accept-Language":"en-US, en;q:0.5"})
  page = requests.get(url, headers=Headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  title = soup.find(id='productTitle').get_text().strip()
  price = soup.find("span", attrs={"class":"a-price-whole"}).get_text().strip()
  return f'Title: {title}, Price: {price}'

if __name__=="__main__":
  app.run()