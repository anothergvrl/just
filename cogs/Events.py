from discord.ext import commands
import random

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('Asu' or 'asu'):
          await message.channel.send('Kau yang asu :kissing:')
        if message.content.startswith('Dih' or 'dih'):
          await message.channel.send('Dah dih dah dih, mantep kaga :open_mouth:')
        if message.content.startswith('anj' or 'anjing' or 'Anj' or 'Anjing'):
          await message.channel.send('Kaya kau lah itu :scream:')
        if message.content.startswith('ibab' or 'babi'):
          await message.channel.send('Males ah maen bawa keluarga :ok_hand:')
        if message.content.startswith('Neng' or 'neng'):
          response = ['Apa sayang?',
                  'Neng cantik disini',
                  'Apasi jelek manggil manggil',
                  'Ada yang bisa eneng bantu?',
                  'Hadir!!!',
                  'AnnyingKeseleo kaka',
                  'Apa cintaku?',
                  'Hoik',
                  'Oit jamet']
          await message.channel.send(f'{random.choice(response)}')
        if message.content.startswith('apa' or 'apakah' or 'Apa' or 'Apakah'):
          response = ['Gatau males :smirk:',
                  'Iya kali :upside_down:',
                  'Sudah pasti :kissing_closed_eyes:',
                  'Tidak :yum:',
                  'Bodo amat :zany_face:',
                  'Nanya mulu jomblo :rage:']
          await message.channel.send(f'{random.choice(response)}')

def setup(bot):
    bot.add_cog(Events(bot))
