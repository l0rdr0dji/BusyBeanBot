import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os

client = discord.Client()
bot = commands.Bot(command_prefix = "+")


@bot.event
async def on_ready():
    await client.change_presence(game=Game(name='Version 0.1 is now up!'))
    print('Ready, Freddy') 
@bot.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='Version 0.1 is now up!'))
    await client.send_message(member, 'Hello! Welcome to the Busy Bean Cafe discord server! I am the bot for this server. Please make sure to verify and read the rules before chatting!')
    print('Sent message to ' + member.name)


@bot.command()
async def on_message(message):
    if message.content == '+sessions':
        await client.send_message(message.channel,'#session-announcements')
    if message.content == '+applications':
        await client.send_message(message.channel,'Check group games for our application center!')
    if message.content == '+Kurt':
        await client.send_message(message.channel,'*CALLS KURT*!!')
    if ('exploit') in message.content:
       await client.delete_message(message)
    if message.content == '+owner':
        await client.send_message(message.channel,'This bot was created by DA_BSSv2 and is developed by DA_BSSv2 and SularMoon')
    if message.content == '+mr-apps':
        await client.send_message(message.channel,'Mr-apps are currently open!:D Check out the application in our application center on the group page. Good luck.')
    if message.content == '+hr-apps':
        await client.send_message(message.channel,'Hr apps are currently closed!D: Look out for more info in #annoucements for the next hr-apps opening.')
    if message.content == '+help':
        em = discord.Embed(description='Here are the commands.')
        em.set_image(url='https://cdn.discordapp.com/attachments/535622552345903115/577634941022765058/unknown.png')
        await client.send_message(message.channel, embed=em)
bot.run(os.environ['token'])
