import discord
import random
from imports import keep_alive
from imports import ball_things
from imports import michael_things

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
  

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #sends pic of fortnite flopper
    if message.content.startswith('!flopper'):
        await message.channel.send('https://cdn.discordapp.com/attachments/793563899201978388/794251087975809084/flopper.png')

    #dissallows Danil to send links from "tenor" domain
    if message.author.id == 227573896306622464 and "tenor" in message.content.lower():
      await message.delete()
      await message.channel.send('stop typing <@227573896306622464>')

    #dissallows Danil to send links from "discordapp" domain
    if message.author.id == 227573896306622464 and "discordapp" in message.content.lower():
      await message.delete()
      await message.channel.send('stop typing <@227573896306622464>')

      #dissallows Danil to send links from "gif" domain
    if message.author.id == 227573896306622464 and "gif" in message.content.lower():
      await message.delete()
      await message.channel.send('stop typing <@227573896306622464>')
    
      #dissallows Chargle to send links from "tenor" domain
    if message.author.id == 420335142930874379 and "tenor" in message.content.lower():
      await message.delete()
      await message.channel.send('stop typing <@420335142930874379>')

    #dissallows Chargle to send links from "discordapp" domain
    if message.author.id == 420335142930874379 and "discordapp" in message.content.lower():
      await message.delete()
      await message.channel.send('stop typing <@420335142930874379>')
    
    #dissallows Chargle to send links from "jpg" domain
    if message.author.id == 420335142930874379 and ".jpg" in message.content.lower():
      await message.delete()
      await message.channel.send('stop typing <@420335142930874379>')

  #dissallows Chargle to send links from "giphy" domain
    if message.author.id == 420335142930874379 and "giphy" in message.content.lower():
      await message.delete()
      await message.channel.send('stop typing <@420335142930874379>')

            #dissallows Summer to send links from "tenor" domain
    if message.author.id == 463728067861282816 and "tenor" in message.content.lower():
      await message.delete()
      await message.channel.send('dummy <@463728067861282816>')

''' toggle strings
#deletes any messages sent in chat
    if message.content.lower():
      await message.delete()

#testing string for gif delete command
    if message.author.id == 497736201575596052 and "gif" in message.content.lower():
      await message.delete()
      await message.channel.send('stop typing <@497736201575596052>')

#deletes messages sent by Chargle bot, kinda crashes the server
    if message.author.id == 794081547451236392:
      await message.delete()
      await message.channel.send('phlopper bot')
'''

keep_alive()
client.run("NzkzNTYwOTMzMDExODE2NDcw.GsU1Sz.HZApARyYlp0zxVJk_4PgyBfZOSXcBEBYXi6ZMY")
