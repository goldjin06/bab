from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4
driver = webdriver.Edge()

driver.get('https://mportal.cau.ac.kr/main.do')
driver.set_window_size(400,1000)



req = driver.page_source
soup = bs4.BeautifulSoup(req, "html.parser")

contents = soup.select("#carteP005 > li > dl > dd > label > .nb-p-04-detail")
print(contents[0].getText(), contents[1].getText())


def breakfast():
    link = driver.find_element('#P005 > div > div > div > div > ol > li > header > div.nb-right.nb-t-right > ol > li:nth-child(1)')
    link.click()
    time.sleep(5)
    contents = soup.select("#carteP005 > li > dl > dd > label > .nb-p-04-detail")
    return(contents)



print(breakfast())

driver.quit()