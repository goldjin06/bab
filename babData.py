from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4
import json
import os

def timeCheck():
    tm = time.localtime(time.time())
    return("%d%02d%d" % (tm.tm_year,tm.tm_mon,tm.tm_mday))

def getMenu(driver,babtime):
    
    link = driver.find_element(By.CSS_SELECTOR,f'#P005 > div > div > div > div > ol > li > header > div.nb-right.nb-t-right > ol > li:nth-child({babtime+1})')
    link.click()
    time.sleep(0.1)
    soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

    dayList = soup.select_one('#P005 > div > div > div > div > ol > li > header > div.nb-left > div > p').getText().split(".")
    title = dayList[0]+dayList[1]+dayList[2]+str(babtime)

    contents = soup.select("#carteP005 > li > dl > dd > label > .nb-p-04-detail")
    
    allMenu = []
    
    for content in contents:

        contentList = content.select("div > div > p > .ng-binding")
        if contentList[2].getText() == "0 원":
            continue
        elif contentList[0].getText() == 'University Club(102관11층)':
            continue

        menuInfo = {"place" : contentList[0].getText(),
                    "time" : contentList[1].getText(),
                    "price" : contentList[2].getText()
                    }

        menuList = content.select("div > p")
        menu = []
        for i in range(3,len(menuList)):
            menu.append(menuList[i].getText())

        if menu != []:
            menuInfo["menu"] = menu
            allMenu.append(menuInfo)

    with open(f"./data/{title}.json","w") as f:
        json.dump({"data" : allMenu},f)
    return(allMenu)



def getBab(day, time): # day여덟자리, time은 0조식 1중식 2석식
    file = f'./data/{day+str(time)}.json'     # 예제 Textfile

    if os.path.isfile(file):
        with open(file,"r") as f:
            data = json.load(f)
        return(data["data"])
    else:

        driver = webdriver.Edge()
        driver.set_window_size(400,1000) # 반응형웹이라서 창 크기
        driver.get('https://mportal.cau.ac.kr/main.do')
        
        click = int(day) - int(timeCheck())
        
        if click > 0:
            link = driver.find_element(By.CSS_SELECTOR,f'#P005 > div > div > div > div > ol > li > header > div.nb-left > div > a.nb-p-time-select-next')
        elif click < 0:
            link = driver.find_element(By.CSS_SELECTOR,f'#P005 > div > div > div > div > ol > li > header > div.nb-left > div > a.nb-p-time-select-prev')

        for i in range(abs(click)):
            link.click()
            
        
        return(getMenu(driver,time))

    

if __name__ == "__main__":
    
    print(getBab("20250430",1))
    
