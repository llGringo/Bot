import discord
from discord.ext import commands
from GoogleSheet import *
 
class Tests(discord.ext.commands.Cog, name='Tests en cours'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="del")
	#@commands.is_owner()
	async def delete(self, ctx, number: int):
		"""Efface le nombre de messages donné."""
		try :
			messages = await ctx.channel.history(limit=number + 1).flatten()
			for each_message in messages:
				await each_message.delete()
		except Exception as e:
			await ctx.send(f'***ERROR:***{type(e).__name__} - {e}')
		else:
			print(f'{number} messages supprimés de {ctx.channel}')

	@commands.command(name="id")
	async def getId(self, ctx):
		try:
			messageID = await ctx.channel.history(oldest_first=True).flatten()
			#setValueSheet(messageID[0].id)
			setValueSheet(978282349970219008)
			await ctx.send(messageID[0].id)
		except Exception as e:
			await ctx.send(f'***ERROR:***{type(e).__name__} - {e}')
		else:
			print(f'{messageID[0].id} message id')



def setup(bot):
	bot.add_cog(Tests(bot))