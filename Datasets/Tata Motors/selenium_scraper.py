from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_elements(By.NAME, "q")
search_box = search_box[0]
search_box.send_keys("Tata Motors 14-01-2019")

search_box.send_keys(Keys.RETURN)

time.sleep(2)

news_tab = driver.find_element(By.XPATH, "//*[contains(text(), 'News')]")
time.sleep(2)
news_tab.click()

news_articles = driver.find_elements(By.XPATH, ".//div[@id = 'search']")
print(news_articles[0].text)

# titles = news_articles.find_elements(By.XPATH, ".//a").get_attribute("href")
# print(titles)

driver.quit()