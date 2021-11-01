from random import choice
from discord.ext import commands, tasks
import discord


class Status(commands.Cog):
    """Em desenvolvimento..."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()

    @tasks.loop(seconds=30)
    async def change_status(self):
        status = ['e ouvindo musiquinhas', 'joguinhos de hentai >///<']
        await self.bot.change_presence(activity=discord.Game(choice(status)))


def setup(bot):
    bot.add_cog(Status(bot))
