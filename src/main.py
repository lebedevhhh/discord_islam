import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from calls import make_random_ayah_request
import os

load_dotenv()
#defining the constants 
TOKEN=os.getenv('TOKEN');
GUILD_ID=os.getenv('GUILD_ID')
CLIENT_ID=os.getenv('CLIENT_ID')


class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object())
        print("Ready!")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            print()


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
bot=commands.Bot(command_prefix='/', intents=intents)

#defining the bot commandss
@bot.command()
async def random_surah_en(ctx):
    content = make_random_ayah_request('en')
    resp=f"**__Oh seeker of the truth here's a random verse for you__** \n```{content['data']['text']}``` [{content['data']['surah']['englishName']}/*{content['data']['surah']['englishNameTranslation']}, verse : {content['data']['number']}*]\n"
    resp+= f"translated by : {content['data']['edition']['englishName']}"
    await ctx.send(resp)

async def random_surah_ar(ctx):
    content=make_random_ayah_request('ar')
    resp=f"**__Oh seeker of the truth! Here's a random verse for you__** \n```{content['data']['text']}``` [{content['data']['surah']['name']}, verse : {content['data']['numberInSurah']}]"
    await ctx.send(resp)

#documentation of all the commands
async def how_to():

    await ctx.send()

async def get_some_country_abbrevations():


bot.run(TOKEN)