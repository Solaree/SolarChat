from server import *
from colorama import Fore

def launch():
    log = input('>>> What do you want to launch:\n| 1: SolarChat::\n| 2: Tokenizer:: ')

    if log == '1':
        #chat_api()
        print('Open bot.py in another terminal window and connect your bot to your server, to make the bridge between SolarChat and Discord!')

    if log == '2':
        #flask_xd()
        print('Open bot.py in another terminal window and run command "!token" to get random token!')
launch()