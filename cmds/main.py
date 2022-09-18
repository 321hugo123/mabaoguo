import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    

   @commands.command()
   async def ping(self,ctx):
      await ctx.send(f"{round(self.bot.latency*1000)}(ms)")

   @commands.command()
   async def 你是誰(self,ctx):
      await ctx.send("我是渾元形意太極門掌門人，馬保國")

   @commands.command()
   async def 你想說什麼(self,ctx):
      await ctx.send("我勸！這位，年輕人，好自為之，好好反思。以後不要再犯這樣的聰明，小聰明，啊。呃，武林，要以和為貴，要講武德，不要搞，窩裡鬥。謝謝朋友們！")

   @commands.command()
   async def 誰是帥哥(self,ctx):
      await ctx.send("kkf是帥哥，香港夜狙沒他帥")
   
   @commands.command()
   async def sayd(self, ctx, msg):
      await ctx.message.delete()
      await ctx.send()

   



def setup(bot):
   bot.add_cog(Main(bot))