import discord, requests

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!token':
        request = requests.get('http://127.0.0.1:5000/token')
        await message.channel.send(request.text)

        while True:
            request()
            await message.channel.send(request.text)
    
    if message.content == '!solarchat':
        request = requests.get('http://127.0.0.1/solarchat')
        await message.channel.send('Connected to HTTP bridge!')
            
        while True:
            await message.channel.send(request.text)

client.run('')