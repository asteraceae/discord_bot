import discord
import json
import pickle

from discord.ext import commands

class User:

    def __init__(self, user, id, images, submittername, submitter):
        self.user = user
        self.id = id
        self.images = images
        self.submittername = submittername
        self.submitter = submitter

class User_Data(commands.Cog):

    __slots__ = ('bot', 'users', 'super')

    def __init__(self, bot):
        self.bot = bot
        self.users = []
        self.super = "bottxt/super.file"
        with (open(self.super, "rb")) as f:
            while True:
                try:
                    self.users.append(pickle.load(f))
                except EOFError:
                    break

    @commands.command(name='adduser')
    async def adduser_(self, ctx, user: discord.User):
        member = user
        id = user.id
        submitter = ctx.author
        for x in self.users:
            if x.id == user.id:
                await ctx.send("This user is already in the database.")
                return
        await ctx.send("Add screenshots? yes/no or STOP to drop entirely")
        while True:
            msg2 = (await self.bot.wait_for("message"))
            if msg2.author == ctx.author:
                if msg2.content.lower() == 'yes':
                    await ctx.send("Send url(s):")
                    while True:
                        urlmsg = (await self.bot.wait_for("message"))
                        if urlmsg.author == ctx.author:
                            url = urlmsg.content
                            break
                    await ctx.send("added")
                    break
                elif msg2.content.lower() == 'no':
                    break
                elif msg2.content.lower() == 'stop':
                    await ctx.send("jeez ok")
                    return
                else:
                    await ctx.send("Invalid input.")
        if "url" in locals():
            u = User(member.name, id, url, submitter.name, submitter.id)
        else:
            u = User(member.name, id, "none", submitter.name, submitter.id)

        with open(self.super , "ab") as f:
            pickle.dump(u, f)
        self.users.append(u)
        await ctx.send("user successfully added to database!")

    @commands.command(name='check')
    async def checkvet_(self, ctx, user:discord.User):
        embedvar = discord.Embed(color=0xABADE8)
        found = False
        for x in self.users:
            if x.id == user.id:
                member = ctx.guild.get_member(x.id)
                try:
                    sub = ctx.guild.get_member(x.submitter).mention
                except:
                    sub = x.submittername + "(no longer in guild)"
                embedvar.add_field(name="User: ", value="{}".format(member.mention), inline=False)
                embedvar.add_field(name="ID: ", value="{}".format(x.id), inline=False)
                embedvar.add_field(name="Account Creation:", value="{}".format(member.created_at), inline=False)
                embedvar.add_field(name="Screenshots:", value="{}".format(x.images), inline=False)
                embedvar.add_field(name="Submitter:", value="{}".format(sub), inline=False)
                await ctx.send(embed=embedvar)
                found = True
        if found == False:
            await ctx.send("Didn't find the user you were looking for.  They may not have been added to the database yet.")
            return

    @commands.command(name='updatess')
    async def updatess_(self, ctx, user:discord.User, ss:str):
        for x in self.users:
            if x.id == user.id:
                x.images = ss
                b = True
                await ctx.send("Updated!")
        if b == False:
            await ctx.send("Didn't find user in database.")
            return
        with open(self.super , "wb") as f:
            for x in self.users:
                pickle.dump(x, f)

    @commands.command(name='userlist')
    async def userlist_(self, ctx):
        str = ""
        for x in self.users:
            member = ctx.guild.get_member(x.id)
            str+= "\n"
            str+="✧ <@{}>, ID: {}".format(x.id, x.id)
        embedvar = discord.Embed(title="List of users in database:", description = str , color=0xABADE8)
        await ctx.send(embed=embedvar)
