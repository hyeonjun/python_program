import discord
from discord.ext import commands
import datetime

from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
import requests


token = 'ODIxNjY4MDEzMzIxMDkzMTUw.YFHD-A.DUuCz3q57Wx8KZ2FajpZRHaYX64'
# client = discord.Client()
game = discord.Game("!도움") # 상태말
intents = discord.Intents.default()
intents.members =True
# 명령어 !로 인식
bot = commands.Bot(command_prefix='!', intents=intents)
# bot = commands.Bot(command_prefix='!',status=discord.Status.online, activity=game)

# global vc

@bot.event
async def on_ready():
    print("봇 시작")

def channel_id(channels):
    position_array = [i.position for i in channels]
    for i in channels:
        if i.position == min(position_array):
            return i

@bot.event
async def on_member_join(member):
    print(channel_id(member.guild.text_channels))
    # channel = discord.utils.get(channel.id, id="id")
    embed = discord.Embed(title=f"서버에 오신 것을 환영합니다.",
                          description=f"디스코드봇 개발 서버", color=0xf3bb76)
    embed.add_field(name=f"봇 개발 시작", value=f"2021년 3월 17일", inline=False)
    embed.add_field(name=f"개발자", value=f"주현준 김기대", inline=False)
    await channel_id(member.guild.text_channels).send(embed=embed)

@bot.event
async def on_member_remove(member):
    msg = "<@{0}> 잘가고~".format(str(member.id))
    await channel_id(member.guild.text_channels).send(msg)

@bot.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("시발")
    if bad >= 0:
        await message.channel.send("욕 안돼")
        await message.delete()
    await bot.process_commands(message)

@bot.command()
async def 시간(ctx):
    now = datetime.datetime.now()
    text = "{}년 {}월 {}일 {}시 {}분".format(now.year, now.month, now.day, now.hour, now.minute)
    # await ctx.send("뭐를")
    await ctx.send(embed=discord.Embed(title="시간", description=text, color=0x00ff00))

@bot.command()
async def 노래(ctx):
    global vc
    try:
        # 음성채널에 봇이 들어갈 수 있게 만듬
        vc = await ctx.message.author.voice.channel.connect()
    except Exception as e:
        await print(e)
        try: # 채널에 유저가 있는지
            await vc.move_to(ctx.message.author.voice.channel)
        except Exception as e: # 유저가 없다면
            await ctx.send("채널에 유저가 없습니다.")
            await print(e)

@bot.command()
async def 조용(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("채널에 접속 중이 아닙니다.")

@bot.command()
async def URL재생(ctx, *, url):

    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(executable="C:\\ffmpeg-4.3.2-2021-02-27-full_build\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")


@bot.command()
async def 재생(ctx, *, msg):
    if not vc.is_playing():
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}

        mozhdr = {
            'User-Agent': 'Mozilla / 5.0 (Windows; U; Windows NT 5.1; en-GB; rv : 1.9.0.3) Gecko / 2008092417 Firefox / 3.0.3'}

        scrape_url = "https://www.youtube.com"
        search_url = "/results?search_query="
        search_hardcode = msg+"+lyrics"

        sb_url = scrape_url + search_url + search_hardcode
        sb_get = requests.get(sb_url, headers=mozhdr)

        soupeddata = bs4.BeautifulSoup(sb_get.content, "html.parser")

        script = soupeddata.find_all("script")
        script_ = str(script[32])

        def extract_url(tag):
            for x in tag.split(','):
                if "watch?" in x:
                    return x

        url_ = extract_url(script_).split(':')[3]
        url_ = url_[1:-1]
        url = 'https://www.youtube.com' + url_
        print(url_)
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(
            embed=discord.Embed(title="노래 재생", description="현재 " + msg + "을(를) 재생하고 있습니다.", color=0x00ff00))
        vc.play(FFmpegPCMAudio(executable="C:\\ffmpeg-4.3.2-2021-02-27-full_build\\bin\\ffmpeg.exe", source=URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 노래가 재생 중이라 노래를 재생할 수 없어요!")

bot.run(token)


















