import discord
from discord.ext import commands
import os

class GestionModules(commands.Cog, name='Gestion modules'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="charger")
    async def load(self, ctx, *, cog: str):
        """Charger modules"""
        try:
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e :
            await ctx.send(f'***ERROR:*** {type(e).__name__} - {e}')
        else:
            await ctx.send('***OK***')

    @commands.command(name="desactiver")
    async def unload(self, ctx, *, cog: str):
        """Desactiver module"""
        try:
            self.bot.unload_extension(f'cogs.{cog}')
        except Exception as e :
            await ctx.send(f'***ERROR*** {type(e).__name__} - {e}')
        else:
            await ctx.send('***OK****')

    @commands.command(name="actualiser")
    async def reload(self, ctx, *, cog: str):
        """Actualiser module"""
        try:
            self.bot.unload_extension(f'cogs.{cog}')
            self.bot.load_extension(f'cogs.{cog}')
        except Exception as e:
            await ctx.send(f'***ERROR*** {type(e).__name__} - {e}')
        else:
            await ctx.send('***OK***')

def setup(bot):
    bot.add_cog(GestionModules(bot))