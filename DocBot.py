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
import discord
from discord.ext import commands


class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
        #self.bot = bot

    async def on_ready(self):
        print("Le bot est prêt !")

    async def on_member_join(member):
        general_channel = client.get_channel(978229594446528565)
        general_channel.send(f"L'utilisateur {member.display_name} a rejoint le serveur !")

    @commands.command(name="del")
    async def delete(ctx, number: int):
        messages = await ctx.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

