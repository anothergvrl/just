import discord
from discord.ext import commands

class Others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='See status ping')
    async def ping(ctx):
      await ctx.send(f':green_circle: {round(bot.latency *1000)} ms', delete_after=5)
    #############END PING
    @commands.command(help='Get Profil Picture')
    async def pp(ctx,member: discord.Member):
      pfp = member.avatar_url
      embed=discord.Embed(
        title="Avatar", 
        description='{}'.format(member),
        colour = discord.Colour.red()
      )
      embed.set_image(url=(pfp))
      embed.set_footer(text='©2020 Aykang All Right Reserved')
      await ctx.send(embed=embed)
    #############END PROFIL PICTURE

def setup(bot):
    bot.add_cog(Others(bot))
