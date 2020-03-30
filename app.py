import discord
import src.command.parser as parser
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

bot.run('NjkzNjExOTk0ODc1NDI4OTQ1.Xn_miw.AIMg2j5q2yIqgCmn0XkZmHpPtEs')