from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4



def getMenu(driver):
    soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
    contents = soup.select("#carteP005 > li > dl > dd > label > .nb-p-04-detail")
    
    allMenu = []
    
    for content in contents:

        contentList = content.select("div > div > p > .ng-binding")
        if contentList[2].getText() == "0 원":
            continue

        menuInfo = {"place" : contentList[0].getText(),
                    "time" : contentList[1].getText(),
                    "price" : contentList[2].getText()
                    }

        menuList = content.select("div > p")
        menu = []
        for i in range(3,len(menuList)):
            menu.append(menuList[i].getText())

        menuInfo["menu"] = menu
        allMenu.append(menuInfo)


    return(allMenu)


def breakfast(driver):
    link = driver.find_element(By.CSS_SELECTOR,'#P005 > div > div > div > div > ol > li > header > div.nb-right.nb-t-right > ol > li:nth-child(1)')
    link.click()
    time.sleep(0.1)
    return(getMenu(driver))

def lunch(driver):
    link = driver.find_element(By.CSS_SELECTOR,'#P005 > div > div > div > div > ol > li > header > div.nb-right.nb-t-right > ol > li:nth-child(2)')
    link.click()
    time.sleep(0.1)
    return(getMenu(driver))

def dinner(driver):
    link = driver.find_element(By.CSS_SELECTOR,'#P005 > div > div > div > div > ol > li > header > div.nb-right.nb-t-right > ol > li:nth-child(3)')
    link.click()
    time.sleep(0.1)
    return(getMenu(driver))

# TODO:
def bab(day, time, driver): # day는 전날은 음수로 다음날은 양수로 받기, time은 0조식 1중식 2석식
    pass

if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.set_window_size(400,1000) # 반응형웹이라서 창 크기
    driver.get('https://mportal.cau.ac.kr/main.do')
    print(breakfast(driver))
    print(lunch(driver))
    print(dinner(driver))

    driver.quit()
