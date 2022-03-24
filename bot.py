import discord
import json
import os
import random
import asyncio
import functools
import itertools
import math
import youtube_dl
import sys
import traceback
import datetime
import music
import poll

from discord.ext import commands
from discord import File
from discord import CategoryChannel
from async_timeout import timeout
from youtube_dl import YoutubeDL
from functools import partial

intents = discord.Intents.all()
print(discord.__version__)
client = commands.Bot(command_prefix = ['!', 'bot '], help_command=None, intents=intents)
client.add_cog(music.Music(client))
client.add_cog(poll.Poll(client))
TOKEN = ''
rc = 0
gc = 0
bc = 0
cache = []

#start

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("with your precious time || !help for commands"))
    print('running')

#backgrounds

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Member')
    await member.add_roles(role)
    id = member.mention
    await client.get_channel(784874874908049448).send("Welcome, {}!".format(id))
    if member.guild.id == 733727250041667734:
        channel = client.get_channel(735645673050865755)
        embedvar = discord.Embed(color=0xABADE8)
        embedvar.set_author(icon_url="https://mpng.subpng.com/20190905/st/transparent-heart-icon-love-icon-5d70d4637284f6.6412339215676754914691.jpg", name="Member Join")
        embedvar.add_field(name="User:", value="{}".format(member.mention), inline=True)
        embedvar.add_field(name="Account Creation:", value="{}".format(member.created_at), inline=True)
        embedvar.set_footer(text="Member ID: {}".format(member.id))
        await channel.send(embed=embedvar)

@client.event
async def on_member_remove(member):
    if member.guild.id == 733727250041667734:
        channel = client.get_channel(735645673050865755)
        embedvar = discord.Embed(color=0xABADE8)
        embedvar.set_author(icon_url="https://mpng.subpng.com/20200312/bjo/transparent-hurt-icon-broken-heart-icon-love-icon-5e6aead1ab5dc6.9266077415840652337019.jpg", name="Member Left")
        embedvar.add_field(name="User:", value="{}".format(member.mention), inline=True)
        embedvar.add_field(name="Account Creation:", value="{}".format(member.created_at), inline=True)
        embedvar.add_field(name="Time Left:", value="{}".format(datetime.datetime.now()), inline=True)
        embedvar.set_footer(text="Member ID: {}".format(member.id))
        await channel.send(embed=embedvar)

@client.event
async def on_message_edit(before, after):
    if before.author.id != 733908926030151710:
        if before.guild.id == 733727250041667734:
            channel = client.get_channel(735645673050865755)

            if not before.attachments:
                bempty = True
            else:
                bempty = False
                str = ""
                for x in before.attachments:
                    if x != before.attachments[0]:
                        str+=" , "
                    str+=x.url

            if bempty == False:
                embedvar = discord.Embed(description="**Before:** {} \n **After:** {}".format(before.content, after.content), color=0xABADE8)
                embedvar.set_author(icon_url="https://cdn0.iconfinder.com/data/icons/medical-and-healthcare-20/24/medical-love-heart-favorite---edit-512.png", name="Edited Message")
                embedvar.add_field(name="User:", value="{}".format(before.author.mention), inline=True)
                embedvar.add_field(name="Channel:", value="{}".format(before.channel.mention), inline=True)
                embedvar.add_field(name="Attachments:", value="{}".format(str), inline = False)
                embedvar.set_footer(text="Message ID: {} | #{}".format(before.id, before.channel.name))
            elif bempty == True:
                embedvar = discord.Embed(description="**Before:** {} \n **After:** {}".format(before.content, after.content), color=0xABADE8)
                embedvar.set_author(icon_url="https://cdn0.iconfinder.com/data/icons/medical-and-healthcare-20/24/medical-love-heart-favorite---edit-512.png", name="Edited Message")
                embedvar.add_field(name="User:", value="{}".format(before.author.mention), inline=True)
                embedvar.add_field(name="Channel:", value="{}".format(before.channel.mention), inline=True)
                embedvar.set_footer(text="Message ID: {} | #{}".format(before.id, before.channel.name))
            if before.content != after.content:
                await channel.send(embed=embedvar)

@client.event
async def on_message_delete(ctx):
    if ctx.author.id != 733787454641012736 and ctx.author.id != 727247475127091322 and ctx.author.id != 430860628132102152:
        if ctx.guild.id == 733727250041667734:
            channel = client.get_channel(735645673050865755)
            if not ctx.attachments:
                empty = True
            else:
                empty = False
                str = ""
                for x in ctx.attachments:
                    if x != ctx.attachments[0]:
                        str+=" , "
                    str+=x.url
            if empty == False:
                embedvar = discord.Embed(description=ctx.content, color=0xABADE8)
                embedvar.set_author(icon_url="https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Close_Icon_Dark-512.png", name="Deleted Message")
                embedvar.add_field(name="User:", value="{}".format(ctx.author.mention), inline=True)
                embedvar.add_field(name="Channel:", value="{}".format(ctx.channel.mention), inline=True)
                embedvar.add_field(name="Attachments:", value="{}".format(str), inline = False)
                embedvar.set_footer(text="Message ID: {} | #{}".format(ctx.id, ctx.channel.name))
            else:
                embedvar = discord.Embed(description=ctx.content, color=0xABADE8)
                embedvar.set_author(icon_url="https://cdn3.iconfinder.com/data/icons/flat-actions-icons-9/792/Close_Icon_Dark-512.png", name="Deleted Message")
                embedvar.add_field(name="User:", value="{}".format(ctx.author.mention), inline=True)
                embedvar.add_field(name="Channel:", value="{}".format(ctx.channel.mention), inline=True)
                embedvar.set_footer(text="Message ID: {} | #{}".format(ctx.id, ctx.channel.name))
            await channel.send(embed=embedvar)



@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == int(733906753489469480):
        if payload.message_id == int(733908926030151710):
            if payload.emoji.name == "💙":
                guild = client.get_guild(payload.guild_id)
                role = discord.utils.get(guild.roles, name='Blue')
                await payload.member.add_roles(role)
            if payload.emoji.name == "💚":
                guild = client.get_guild(payload.guild_id)
                role = discord.utils.get(guild.roles, name='Green')
                await payload.member.add_roles(role)
            if payload.emoji.name == "💛":
                guild = client.get_guild(payload.guild_id)
                role = discord.utils.get(guild.roles, name='Yellow')
                await payload.member.add_roles(role)
    if payload.emoji.name == "⭐":
        channel = client.get_channel(payload.channel_id)
        if channel.id == 748002071910940713 or channel.id == 748002123496685789 or channel.id == 748002307727294504 or channel.id == 767786477748486184:
            return
        message = await channel.fetch_message(payload.message_id)
        count = 0
        for reaction in message.reactions:
            if reaction.emoji == "⭐":
                count = reaction.count
        if count == 3:
            await createboard(message)

async def createboard(message):
    empty = False
    user = message.author
    channel = client.get_channel(748025541768249474)
    date = message.created_at
    date = date.today().strftime('%Y-%m-%d')
    if not message.attachments:
        empty = True
    else:
        image = message.attachments[0].url
    if empty == False:
        embedvar = discord.Embed(description="{}".format(message.content), color=0xABADE8)
        embedvar.set_image(url=image)
        embedvar.set_author(icon_url=user.avatar_url, name=user)
        embedvar.set_footer(text="{} | #{}".format(date, message.channel.name))
    else:
        embedvar = discord.Embed(description="{}".format(message.content), color=0xABADE8)
        embedvar.set_author(icon_url= user.avatar_url, name=user)
        embedvar.set_footer(text="{} | #{}".format(date, message.channel.name))
    await channel.send(embed=embedvar)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id == int(733906753489469480):
        if payload.message_id == int(733908926030151710):
            if payload.emoji.name == "💙":
                guild = client.get_guild(payload.guild_id)
                role = discord.utils.get(guild.roles, name='Blue')
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role)
            if payload.emoji.name == "💚":
                guild = client.get_guild(payload.guild_id)
                role = discord.utils.get(guild.roles, name='Green')
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role)
            if payload.emoji.name == "💛":
                guild = client.get_guild(payload.guild_id)
                role = discord.utils.get(guild.roles, name='Yellow')
                member = guild.get_member(payload.user_id)
                await member.remove_roles(role)



@client.event
async def on_message(ctx):
    nctx = ctx.content.lower()
    if nctx == "jesus" or nctx == "jesus!" or nctx == "jesus.":
        await ctx.channel.send("jesus indeed")
    if nctx == "good bot" or nctx == "good bot." or nctx == "good bot!":
        await ctx.channel.send("Thanks!")
        await addscore("good")
    if nctx == "bad bot" or nctx == "bad bot." or nctx == "bad bot!":
        await ctx.channel.send("I'm sorry!")
        await addscore("bad")
    if ctx.guild is None and ctx.author != client.user:
        person = await client.fetch_user(430860628132102152)
        person2 = ctx.author
        channel = await person2.create_dm()
        channel2 = await person.create_dm()
        #await channel.send("Thanks for your message; it has been received! :D")
        empty = False
        if not ctx.attachments:
            empty = True
        else:
            image = ctx.attachments[0].url
        if empty == False and ctx.content is None:
            await channel2.send("{}".format(image))
            await channel2.send("from: {}, ID: {}".format(ctx.author, ctx.author.id))
        elif empty == True and ctx.content is None:
            await channel2.send("\n############################################################################################\n")
            await channel2.send("{}".format("no message, bug occurred"))
            await channel2.send("from: {}, ID: {}".format(ctx.author, ctx.author.id))
            await client.process_commands(ctx)
        elif empty == False:
            await channel2.send("\n############################################################################################\n")
            await channel2.send("{}\n{}".format(ctx.content, image))
            await channel2.send("from: {}, ID: {}".format(ctx.author, ctx.author.id))
        else:
            await channel2.send("\n############################################################################################\n")
            await channel2.send("{}".format(ctx.content))
            await channel2.send("from: {}, ID: {}".format(ctx.author, ctx.author.id))
    await client.process_commands(ctx)

#useful commands
@client.command()
async def edit(ctx, id, *, msg):
    if ctx.author.guild_permissions.administrator:
        await ctx.message.delete()
        channel = client.get_channel(ctx.channel.id)
        message = await channel.fetch_message(id)
        await message.edit(content = msg)

@client.command()
async def reply(ctx, id, *, msg):
    if ctx.author.guild_permissions.administrator:
        await ctx.message.delete()
        channel = client.get_channel(ctx.channel.id)
        message = await channel.fetch_message(id)
        await message.reply(f'{msg}')

@client.command()
async def addrxn(ctx, id, emoji):
    if ctx.author.guild_permissions.administrator:
        await ctx.message.delete()
        channel = client.get_channel(ctx.channel.id)
        message = await channel.fetch_message(id)
        await message.add_reaction(emoji = emoji)

@client.command(pass_context=True)
async def purge(ctx, limit: int):
    if ctx.author.guild_permissions.administrator:
            await ctx.channel.purge(limit = limit + 1)
            await ctx.send('Cleared {} messages, command activated by {}.'.format(limit, ctx.author.mention), delete_after = 10)
    else:
        await ctx.send("You're not admin.", delete_after = 10)

@client.command()
async def help(ctx):
    embedVar = discord.Embed(title="Help ٩(｡•́‿•̀｡)۶", description="List of Bot's commands!", color=0xABADE8)
    if ctx.author.guild_permissions.administrator:
        embedVar.add_field(name="✧ purge #", value="Admin only. # denotes any number.  Clears messages from channel. ", inline=False)
    embedVar.add_field(name="✧ music player commands", value="play, join/connect, remove/clear #, queue/q, skip, stop, pause, resume, np/current \nType !musichelp for more info on these commands.", inline=False)
    embedVar.add_field(name="✧ score", value="Show's bot's good/bad bot score. Simply say 'good bot' or 'bad bot' to change its score.", inline=False)
    embedVar.add_field(name="✧ 8ball (QUESTION)", value="Generates 8 ball to answer your question", inline=False)
    embedVar.add_field(name="✧ say (MESSAGE)", value="The bot repeats your message.  Note that emojis from outside this server will not reproduce properly.", inline=False)
    embedVar.add_field(name="✧ poll ([title, question, question] in quotes)", value="Generates a poll for users to react to.  Type !pollhelp to view how to format.", inline=False)
    embedVar.add_field(name="✧ random commands to try", value="nou, agreewme, sendpfp", inline=False)
    embedVar.add_field(name="✧ acceptable trigger commands", value="!, bot (space)", inline=False)
    embedVar.set_footer(text="drop suggestions in #bot-requests")
    await ctx.channel.send(embed=embedVar)

@client.command()
async def musichelp(ctx):
    embedVar = discord.Embed(title="Music Help ♫꒰･◡･๑꒱", description="List of bot's commands!", color=0xABADE8)
    embedVar.add_field(name="✧ music player commands", value="play, join/connect, remove/clear #, queue/q, skip, stop, pause, resume, np/current \nType !musichelp for more info on these commands.", inline=False)
    embedVar.add_field(name="✧ play (song)", value="Adds song to bot's queue.  Also will automatically make the bot join voice channel.  You must be in a voice channel for this command to work.", inline=False)
    embedVar.add_field(name="✧ join/connect", value="Makes bot join the voice channel you're in.", inline=False)
    embedVar.add_field(name="✧ remove/clear #", value="Removes a specific song from queue. # denotes position in queue.", inline=False)
    embedVar.add_field(name="✧ queue/p", value="Shows full queue of songs.", inline=False)
    embedVar.add_field(name="✧ skip", value="Skips current song.", inline=False)
    embedVar.add_field(name="✧ stop", value="Disconnects bot from voice chat and clears queue.", inline=False)
    embedVar.add_field(name="✧ pause", value="Pauses current song.", inline=False)
    embedVar.add_field(name="✧ resume", value="Resumes paused song.", inline=False)
    embedVar.add_field(name="✧ np/current", value="Shows what's now playing.", inline=False)
    embedVar.set_footer(text="drop suggestions in #bot-requests")
    await ctx.channel.send(embed=embedVar)

@client.command()
async def score(ctx):
    gc = int(await getscore("good"))
    bc = int(await getscore("bad"))
    embedVar = discord.Embed(title="bot's Report Card📈", color=0xABADE8)
    embedVar.add_field(name="Good bot count: ", value=f'+{gc}', inline=True)
    embedVar.add_field(name="Bad bot count: ", value=f'-{bc}', inline=True)
    if gc - bc >= 0:
        symbol = "+"
    else:
        symbol = "-"
    embedVar.add_field(name="Overall count: ", value=f'{symbol}{gc - bc}', inline=True)
    await ctx.channel.send(embed=embedVar)


@client.command()
async def dm(ctx, id, *, msg:str):
    if ctx.author.id == 430860628132102152:
        await ctx.message.delete()
        member = await client.fetch_user(id)
        channel = await member.create_dm()
        await channel.send(msg)
        await ctx.send("Message sent", delete_after = 10 )

async def getscore(str):
    file = "bottxt/score.txt"
    lines = ""
    with open(file) as f:
        lines = f.readlines()
    list = lines
    if str == "good":
        return list[0]
    elif str == "bad":
        return list[1]

async def addscore(s):
    gc = int(await getscore("good"))
    bc = int(await getscore("bad"))
    file = "bottxt/score.txt"
    wr = open(file, 'w')
    if s == "good":
        gc += 1
        ngc = str(gc)
        nbc = str(bc)
        wr.write(ngc)
        wr.write("\n")
        wr.write(nbc)
    elif s == "bad":
        bc += 1
        ngc = str(gc)
        nbc = str(bc)
        wr.write(ngc)
        wr.write("\n")
        wr.write(nbc)
#status message creators

@client.command()
async def agreewme(ctx):
    await ctx.message.delete()
    list = ["Yes", "yes absolutely", "i saw it myself", "i saw it with my own eyes 100% agree", "yes I agree", "i agree with her 100%", "yup"]
    id = random.randint(0, len(list) - 1)
    await ctx.trigger_typing()
    await ctx.send(list[id])

@client.command()
async def nou(ctx):
    await ctx.message.delete()
    emoji = "<:reverse:733778903847403622>"
    await ctx.send("no u")
    await ctx.send(emoji)

#dumb but cool text commands
@client.command()
async def nuclear(ctx, mem: discord.Member, *, category: CategoryChannel):
    if ctx.author.id == 430860628132102152:
        await ctx.message.delete()
        guild = client.get_guild(733727250041667734)
        channels = guild.category.channels
        for channel in channels:
            async for message in channel.history(limit = 100000000):
                if message.author == ctx.author:
                    await message.delete()
        if ctx.author.id == 430860628132102152:
            member = await client.fetch_user(430860628132102152)
            channel = await member.create_dm()
            await channel.send("Success, deleted messages of {}".format(mem))

@client.command()
async def spam(ctx, mem: discord.Member):
    if ctx.author.id == 430860628132102152:
        await ctx.message.delete()
        guild = client.get_guild(733727250041667734)
        channels = guild.text_channels
        for channel in channels:
            async for message in channel.history(limit = 100000000):
                if message.author == mem:
                    await message.delete()
        string = ""
        if ctx.author.id == 430860628132102152:
            member = await client.fetch_user(430860628132102152)
            channel = await member.create_dm()
            await channel.send("Success, deleted messages of {}".format(mem))

@client.command()
async def say(ctx, *, msg:str):
    await ctx.message.delete()
    await ctx.trigger_typing()
    await ctx.send(msg)

@client.command()
async def say2(ctx, channel:discord.TextChannel, *, msg):
    await ctx.message.delete()
    c = client.get_channel(channel.id)
    await c.trigger_typing()
    await c.send(msg)
    await client.get_channel(735645673050865755).purge(limit = 1)


@client.command(name = '8ball')
async def magic(ctx, *, msg):
    path ='bottxt/images/8ball/'
    files = os.listdir(path)
    index = random.randrange(0, len(files))
    string = "bottxt/images/8ball/{}".format(files[index])
    file2 = discord.File(f"{string}", filename="image.gif")
    embedvar = discord.Embed(description = f"You asked: **{msg}**\n\nMy answer...", color=0xABADE8)
    embedvar.set_author(icon_url="https://p7.hiclipart.com/preview/90/451/830/magic-8-ball-8-ball-pool-eight-ball-crystal-ball-8.jpg", name="Magic 8 Ball (∩｡･ｏ･｡)っ━━━★ﾟ｡'")
    embedvar.set_image(url="attachment://image.gif")
    await ctx.send(file=file2, embed=embedvar)

@client.command()
async def sendpfp(ctx):
    await ctx.send(ctx.author.avatar_url)

client.run(TOKEN)
