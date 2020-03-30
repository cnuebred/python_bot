import discord
from src.command import parser
import json
with open('config.json') as json_file: 
    token = json.load(json_file)['token']

bot = discord.Client()
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$'):
       await parser.mainParser(bot, message)

bot.run(token)