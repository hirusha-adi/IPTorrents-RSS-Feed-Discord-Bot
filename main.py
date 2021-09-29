import iptrss.others.installerm as melloins
try:
    import discord
    from discord.ext import commands
except:
    melloins.pip_install("discord")
    import discord
    from discord.ext import commands
import asyncio
try:
    import requests
except:
    melloins.pip_install("discord")
    import requests
from iptrss.web.keep_alive import keep_alive
import iptrss.database.get_main as getbase
import xml.etree.ElementTree as ET
from platform import python_version

bot_version = getbase.BotMain.BOT_VERSION
bot_prefix = getbase.BotMain.MSG_PREFIX
bot_creator_name = getbase.BotMain.CREATOR_NAME
bot_token = getbase.BotMain.TOKEN

client = commands.Bot(command_prefix = bot_prefix)

first_item_info = []


@commands.has_permissions(administrator=True)
@client.command(brief="Enable RSS FEED")
async def startrss(ctx):

    PAUSE_TIME = 300
    TEMP_XML_FILE = "iptrss/movieinfo/file.xml"
    LAST_MOVIE_FILE = "iptrss/movieinfo/lastmovie.txt"
    FEED_URL = "https://iptorrents.com/t.rss?u=315854;tp=07d2b12c3465a70e02608702b3f65c3a;48;7;20;38;100;101;89;68;62;6;90;87;54;22;99;4;5;66;65;79;23;55;25;26;82;24;83;download"
    
    await ctx.send(f"+ Starting to send latest updates to **{ctx.channel.name} | {ctx.channel.id}**")

    while True:
        data = requests.get(FEED_URL).content
        with open(TEMP_XML_FILE, "w", encoding="utf-8") as fmake1:
            fmake1.write(data.decode())
        
        tree = ET.parse(TEMP_XML_FILE)
        root = tree.getroot()

        global first_item_info

        j = 0
        for elem in root:
            for subelem1 in elem:
                for i in subelem1:
                    if j <= 3:
                        # print(i.text)
                        first_item_info.append(f"{i.text}")
                        j += 1
                    else:
                        break

        print("[+] Latest request:", first_item_info[0])

        with open(LAST_MOVIE_FILE, "r", encoding="utf-8") as lastmvname:
            last_movie_name = lastmvname.read()
        
        if last_movie_name == first_item_info[0]:
            print("[-] The latest title has not been updated yet")
        else:
            print("[+] New latest title:", first_item_info[0])
            with open(LAST_MOVIE_FILE, "w", encoding="utf-8") as newlastmv:
                newlastmv.write(first_item_info[0])
            
            embed=discord.Embed(title="IPTorrents RSS Feed", color=0xff6600)
            embed.set_author(name="Mello", icon_url="https://cdn.discordapp.com/attachments/877796755234783273/892817965047750686/DeathNoteMello.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877796755234783273/892817965047750686/DeathNoteMello.png")
            embed.add_field(name="Movie Title:", value=f"first_item_info[0]", inline=False)
            embed.add_field(name="Link:", value=f"first_item_info[1]", inline=False)
            embed.add_field(name="Published Date", value=f"first_item_info[2]", inline=False)
            embed.add_field(name="Description", value=f"first_item_info[3]", inline=False)
            await ctx.send(embed = embed)

            print("[+] Sent embed")
            
        first_item_info.clear()

        await asyncio.sleep(PAUSE_TIME)


@client.event
async def on_ready():
    print(f'Discord.py API version: {discord.__version__}')
    print(f'Python version: {python_version()}')
    print(f'Logged in as {client.user} | {client.user.id}')


@client.event
async def on_message(message):
    if client.user == message.author:
        return

    await client.process_commands(message)



keep_alive()
client.run(bot_token)
