import discord
from dotenv import load_dotenv
import os
import babData as bab
from selenium import webdriver


driver = webdriver.Edge()
driver.set_window_size(400,1000) # 반응형웹이라서 창 크기
driver.get('https://mportal.cau.ac.kr/main.do')
a = [bab.breakfast(driver), bab.lunch(driver), bab.dinner(driver)]

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} good")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond(f'''{a}''')


bot.run(os.getenv("TOKEN"))