from discord.ext import commands

class CustomBotClient(commands.Bot):

	async def on_ready(self):
		print (f'{self.user.name} est connecté au Discord !')
