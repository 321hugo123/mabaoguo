import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
   @commands.Cog.listener()
   async def on_member_join(self, member):
    channel = self.bot.get_channel(int(jdata["Welcome_channel"]))
    await channel.send(f"{member}加入了")

   @commands.Cog.listener()
   async def on_member_remove(self, member):
    channel = self.bot.get_channel(int(jdata["Leave_channel"]))
    await channel.send(f"{member}離開了")

   @commands.Cog.listener()
   async def on_message(self, msg):
      keyword = (jdata["keyword"])
      if msg.content in keyword and msg.author != self.bot.user:
         await msg.channel.send("邊撚個講粗口")
 
def setup(bot):
   bot.add_cog(Event(bot))