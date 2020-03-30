
import src.command.container as container

async def mainParser(bot, msg):
    params = msg.content.split(' ')
    command = (list(params)[0])[1:]
    print(command)
    print(container.container['user'][command])