import discord
from discord.ext import commands
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
	async def getId(self, ctx, numbre: int):
		try:
			messageID = ctx.channel.history(limit=number + 1).id()
			await ctx.send(messageID)
		except Exception as e:
			await ctx.send(f'***ERROR:***{type(e).__name__} - {e}')
		else:
			print(f'{messageID} message id')



def setup(bot):
	bot.add_cog(Tests(bot))