import discord

TOKEN = 'NDQ1NjQwMTYyNTkzMjEwMzc5.Ddta_w.ZquwLXCL-U36WJdR7OBrZJan3NY'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'BONJOUR JE SUIS MEILLEUR QUE RAPHITOU'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
