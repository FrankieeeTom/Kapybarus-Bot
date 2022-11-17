from ast import Await
import discord

TOKEN = 'secret'

client = discord.Client()

@client.event
async def on_ready():
    print('You have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)

    channel = str(message.channel.name)
    print(f'{username}: {user_message}   ({channel})')

    if message.author == client.user:
        return
        
    if message.channel.name == 'boťáci':
        if user_message == '!smrdíš':
            await message.channel.send(f'ne to ty smrdíš {username}!')
            return
        elif user_message == 'AI':
            await message.channel.send(f'/imagine prompt:dog in space/imagine prompt:dog in space')
            return
        elif user_message == '!DEBYL':
            await message.channel.sendf(f"")
            return
        elif user_message == '!blbec <@768852526514569256>':
            await message.channel.send(f'<@768852526514569256> Není blbec {username}! ')
            return
            
            
    #     if user_message.lower() == '':
    #        await message.channel.send('{username} ty jsi ale sprostý! <@&956484462613516308> ti ukážou co je to porušení pravidel!')
    #        return
        if user_message.lower() == '!rick':
            await message.channel.send('https://cdn.discordapp.com/attachments/970081996527251546/1020634283754397817/rick-astley.gif')
            return
        if user_message.lower() == '<@947562598969245777>':
            await message.channel.send('TO JSEM JÁ!')
            return    
        if user_message.lower() == 'test':
            await message.channel.send('/imagine prompt:dog in space')
            return
    client.run(TOKEN)
