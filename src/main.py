import discord
from dotenv import load_dotenv
from discord.ext import commands
from calls import make_random_ayah_request
import os

load_dotenv()
#defining the constants 
TOKEN=os.getenv('TOKEN');
CLIENT_ID=os.getenv('CLIENT_ID')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
# client = MyClient(intents=intents)
bot=commands.Bot(command_prefix='/', intents=intents)

#defining the bot commandss
@bot.command()
async def random_surah_en(ctx):
    content = make_random_ayah_request("en")
    resp=f"Oh seeker of the truth here's a random verse for you \n{content['data']["text"]} [{content["surah"]["englishName"]}/{content["surah"]["englishNameTranslation"]}, verse : {content["data"]["number"]}]\n"
    resp+= f"translated by : {content['edition']['englishName']}"
    ctx.send(resp)


async def random_surah_ar(ctx):
    content=make_random_ayah_request("ar")
    resp=f"Oh seeker of the truth! Here's a random verse for you \n{content['data']["text"]} [{content["surah"]["name"]}, verse : {content['numberInSurah']}]"
    ctx.send(resp)

bot.run(TOKEN)