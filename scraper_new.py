import requests
from bs4 import BeautifulSoup
import datetime as dt
from collections import defaultdict
import csv
import time

q="Tata Motors"
start_date=dt.date(2019,3,14)
news_data=defaultdict(list)

def scrape_news(q,date):
    day=date.day
    month=date.month
    year=date.year
    url=f'https://news.google.com/search?q={q}+{day}-{month}-{year}&hl=en-IN&gl=IN&ceid=IN:en'
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser') 
    #write the soup to a file
    #find all a tags of class "JtKRv" 
    #these contain the titles of the news articles
    titles=soup.find_all('a',class_="JtKRv")
    #print the top 3 titles
    date_str=f"{day}-{month}-{year}"
    for title in titles[:3]:
        news_data[date_str].append(title.text)

#iterate over the dates
for i in range(30):
    scrape_news(q,start_date)
    start_date+=dt.timedelta(days=1)
    #sleep for 1 second to avoid getting blocked
    time.sleep(1)

#write the dictionary to a csv file with date and title as columns
with open('tata_motors_news.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Date', 'Title'])
    for date in news_data:
        for title in news_data[date]:
            writer.writerow([date, title])

