from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_elements(By.NAME, "q")
search_box = search_box[0]
search_box.send_keys("Tata Motors 14-03-2019")

search_box.send_keys(Keys.RETURN)

time.sleep(2)

news_tab = driver.find_element(By.XPATH, "//a[@class='LatpMc nPDzT T3FoJb']")
time.sleep(2)
news_tab.click()

time.sleep(2)

news_articles = driver.find_elements(By.XPATH, "//div[@class='tF2Cxc']")

date_format = "%b %d, %Y"

for article in news_articles:
    date_element = article.find_element(By.XPATH, ".//span[@class='WG9SHc']")
    article_date = datetime.datetime.strptime(date_element.text, date_format).date()

    one_week_ago = datetime.datetime.now().date() - datetime.timedelta(days=7)
    if article_date >= one_week_ago:
        title_element = article.find_element(By.XPATH, ".//h3[@class='ipQwMb ekueJc RD0gLb']")
        title = title_element.text
        link_element = article.find_element(By.XPATH, ".//a[@class='DY5T1d']")
        link = link_element.get_attribute("href")
        print("Title:", title)
        print("Link:", link)
        print("Date:", article_date)
        print()
    else:
        break

driver.quit()