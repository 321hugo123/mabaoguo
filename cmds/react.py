import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("setting.json",mode="r",encoding="utf8")as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

   @commands.command()
   async def rickroll(self, ctx):
       random_pic = random.choice(jdata["pic"])
       pic = discord.File(random_pic)
       await ctx.send(file= pic)

   @commands.command()
   async def 保國(self, ctx):
       random_pic = random.choice(jdata["baoguo"])
       pic = discord.File(random_pic)
       await ctx.send(file= pic)
    
def setup(bot):
    bot.add_cog(React(bot))
