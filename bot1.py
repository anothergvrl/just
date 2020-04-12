#######CREDIT BY AYKANG########
#######PLEASE CONTACT ME IF YOU WANT RECODE########
import asyncio
import functools
import itertools
import math
import random

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
bot = commands.Bot('.', description='ENENG V 1.0.1.')
bot.remove_command('help')
#############END STATUS EVENT
extensions = ['cogs.SpoonRadio', 'cogs.Events', 'cogs.Music', 'cogs.Help', 'cogs.Others']
if __name__ ==  '__main__':
    for ext in extensions:
        bot.load_extension(ext)
        bot.reload_extension(ext)
bot.run('Njg5MTAyODU5ODA3MDk2ODYy.XpIHmw.KFWk44EZQAkFNB5uV8kVs0FYDqs')
