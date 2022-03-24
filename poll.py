import discord
import re

from discord.ext import commands

class Poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.options = []

    @commands.command(name='poll')
    async def pollparse_(self, ctx, *, msg:str):
        string = msg
        list = re.findall(r'\"(.*?)\"', string)
        emoji = ['', '❤','🧡','💛','💚','💙','💜','🤎','🖤','🤍','💖','💓','💗','💕','❣','💔']
        self.options = list
        if len(self.options) < 1 or len(self.options) == 2:
            await ctx.send("You must provide at least 2 options in order to create a poll.  Type !pollhelp to view how to format.")
            return
        elif len(self.options) == 1:
            message = await ctx.send(f'**POLL: {self.options[0]} ** :bar_chart:')
            await message.add_reaction(emoji='👍')
            await message.add_reaction(emoji='👎')
        else:
            chart = self.createpoll_(list)
            message = await ctx.send(f'**POLL: {self.options[0]} ** :bar_chart:', embed = chart)
            for x in range (1, len(self.options)):
                await message.add_reaction(emoji=emoji[x])

    def createpoll_(self, list):
        embedVar = discord.Embed(color=0xABADE8)
        emoji = ['', '❤','🧡','💛','💚','💙','💜','🤎','🖤','🤍','💖','💓','💗','💕','❣','💔']
        value = ''
        for x in range(1, len(self.options)):
            value += f'{emoji[x]} = {self.options[x]}\n'
        embedVar.add_field(name = 'Options:', value=value, inline=False)
        return embedVar
        #value=f'{emoji[x]} = {self.options[x]}

    @commands.command(name='pollhelp')
    async def usage_(self, ctx):
        s1 = 'To make a multi option poll: `!poll "TITLE" "A" "B" "C"` (options are limitless)'
        s2 = 'To make a YES\\NO poll: `!poll "TITLE"`'
        embedVar = discord.Embed(title="How to use the polling function! (╯°□°）╯︵ ┻━┻", description=f'💙 {s1}\n💜 {s2} ', color=0xABADE8)
        await ctx.send(embed=embedVar)
