import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from calls import make_random_ayah_request, get_hadith
import os

STRING_RESPECT="may allah be pleased with him"
load_dotenv()
#defining the constants 
TOKEN=os.getenv('TOKEN');
GUILD_ID=os.getenv('GUILD_ID')
CLIENT_ID=os.getenv('CLIENT_ID')
API_KEY=os.getenv('API_KEY')


class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object())
        print("Ready!")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
bot=commands.Bot(command_prefix='/', intents=intents)

#defining the bot commandss
@bot.command()
async def random_surah_en(ctx):
    content = make_random_ayah_request('en')
    resp=f"**__Oh seeker of the truth here's a random verse for you__** \n```{content['data']['text']}``` [{content['data']['surah']['englishName']}/*{content['data']['surah']['englishNameTranslation']}, verse : {content['data']['number']}*]"
    resp+= f" translated by : {content['data']['edition']['englishName']}"
    await ctx.send(resp)

@bot.command()
async def random_surah_ar(ctx):
    content=make_random_ayah_request('ar')
    resp=f"**__Oh seeker of the truth! Here's a random verse for you__** \n```{content['data']['text']}``` [{content['data']['surah']['name']}, verse : {content['data']['numberInSurah']}]"
    await ctx.send(resp)

#documentation of all the command
@bot.command()
async def how_to(ctx):
    str_ = "to get a random verse from the quran (english): ``/random_surah_en``\n"
    str_ += "to get a random verse from the quran (arabic): ``/random_surah_ar``\n"
    str_ += "to get a random hadith from the two main source : ``/random_hadith``"
    await ctx.send(str_)

@bot.command()
async def random_hadith(ctx):
    json_response=get_hadith()
    str_=f"**__Oh seeker of the truth! Here's a random hadith for you__**\n```{json_response['hadithEnglish']}```"
    str_+=f"*Narrated by {json_response['englishNarrator'].split(' ')[1]} {STRING_RESPECT}, Chapter {json_response['chapterId']} {json_response['chapter']['chapterEnglish']}, Book {json_response['book']['bookName']}*"
    await ctx.send(str_)

bot.run(TOKEN)