import pandas as pd
import numpy as np

async def mainNode(bot, msg):
    params = msg.content.split(' ')
    command = (list(params)[0])[1:]
    container = pd.read_csv('src/command/container.csv')
    if not(command in list(container['command'])):return print('I cant find this command')
    commandModule = container[container['command'] == command].values[0]
    print()

async def mainParser(bot, msg):
    getCommandModule = await mainNode(bot, msg)