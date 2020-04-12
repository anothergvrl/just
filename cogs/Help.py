import discord
from discord.ext import commands

class Help(commands.Cog):
    def _init_(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(help='Credit of bot')
    async def help(self, ctx):
      embed = discord.Embed(
        title = 'ENENG V1',
        url = 'https://www.instagram.com/eneng.bot/',
        description = 'Bot for having fun\nUse carefully and peace\nPlease contact me if the bot not working\n==================================',
        colour = discord.Colour.red()
      )

      embed.set_footer(text='©2020 Aykang All Right Reserved')
      embed.add_field(name='Commands', value='Use this symbol (.) for running the bot.', inline=True)
      embed.add_field(name='All About Eneng', value='(ping) To see server status.\n(pp) To get profil picture member.\n(help) To see this commands.', inline=True)
      embed.add_field(name='Spoon Radio', value='List Feature:\n1.(neng_anu) To Uproom Spoon Radio\n2.(neng_keluarin) To Leave The Bot From Live\n3.(neng_gantiin) To Change ID Spoon Radio', inline=True)
      embed.add_field(name='Music', value='List Command:\n(join) Join a voice channel\n(leave) Leave a voice channel and Clear queue\n(loop) Loops the currently playing song\n(now) Displays the currently playing song\n(pause) Paused the currently playing song\n(queue) Shows the players queue\n(remove) Removes a song from the queue\n(resume) Resumes a currently paused song\n(shuffle) Shuffles the queue\n(skip) Skipped the currently playing song\n(stop) Stop playing song and Clear queue\n(summon) Summon the bot to a voice channel\n(volume) Set the volume of the player', inline=True)

      await ctx.send(embed=embed, delete_after=30)
      
def setup(bot):
    bot.add_cog(Help(bot))
