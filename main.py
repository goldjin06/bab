import discord
from dotenv import load_dotenv
import os
import babData as bab
from selenium import webdriver
import time
 
load_dotenv()
bot = discord.Bot()

class status():
    def __init__(self):
        self.lastCheckTime = timeCheck()
        pass

def timeCheck():
    tm = time.localtime(time.time())
    return("%d%02d%d" % (tm.tm_year,tm.tm_mon,tm.tm_mday))

def refresh():
    lastCheckTime = timeCheck()
    a = [bab.breakfast(driver), bab.lunch(driver), bab.dinner(driver)]

@bot.event
async def on_ready():
    print(f"{bot.user} good")

def displayDic(menu):
    printStr = ""
    for place in range(len(menu)):
        nowMenu = menu[place]
        menuStr = ""
        for i in nowMenu["menu"]:
            menuStr = menuStr +  "- " + i + "\n"

        printStr = printStr + f'''
## {nowMenu["place"]} ({nowMenu["price"]})
{nowMenu["time"]}
{menuStr}''' + '\n'
        
    return(printStr)


class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="조식", style=discord.ButtonStyle.grey, emoji="🌅") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_breakfast(self, button, interaction):
        await interaction.response.send_message(displayDic(a[0])) # Send a message when the button is clicked

    @discord.ui.button(label="중식", style=discord.ButtonStyle.grey, emoji="☀️") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_lunch(self, button, interaction):
        await interaction.response.send_message(displayDic(a[1]))
    
    @discord.ui.button(label="석식", style=discord.ButtonStyle.grey, emoji="🌙") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_dinner(self, button, interaction):
        await interaction.response.send_message(displayDic(a[2]))

@bot.slash_command(name="todaybab", description="밥 알려줌")
async def hello(ctx: discord.ApplicationContext):
    if lastCheckTime != timeCheck():
        refresh()
    await ctx.respond("언제 밥?", view = MyView())

if __name__ == "__main__":
    driver = webdriver.Edge()
    driver.set_window_size(400,1000) # 반응형웹이라서 창 크기
    driver.get('https://mportal.cau.ac.kr/main.do')


    global a
    global lastCheckTime
    lastCheckTime = timeCheck()
    a = [bab.breakfast(driver), bab.lunch(driver), bab.dinner(driver)]

    bot.run(os.getenv("TOKEN"))