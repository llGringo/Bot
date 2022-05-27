#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      fabiod
#
# Created:     23/05/2022
# Copyright:   (c) fabiod 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python3
import discord
from clients.custom_bot_client import CustomBotClient
from cogs.gestion_modules import GestionModules
from cogs.tests import Tests
from dotenv import load_dotenv
import os

def main():
    load_dotenv(dotenv_path=".config")
    TOKEN = os.getenv("TOKEN")
    
    intents = discord.Intents.default()
    intents.members = True

    bot = CustomBotClient(
        command_prefix='!',
        owner_id = 265856034621489152,
        intents=intents
    )

    initial_extensions = ['cogs.gestion_modules',
                            'cogs.tests']

    for extension in initial_extensions:
        bot.load_extension(extension)


    bot.run(TOKEN)

if __name__ == '__main__':
    main()