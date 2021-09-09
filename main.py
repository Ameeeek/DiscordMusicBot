import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
client = commands.Bot(command_prefix='?')
client.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'serah',
        'region': 'singapore'
    }
]
@client.event
async def on_ready():
    activity=discord.Activity(type=discord.ActivityType.listening, name='Vibing')
    await client.change_presence(activity=activity)
    print('Aye aye Captain!')
    client.load_extension('dismusic')



keep_alive()
client.run(os.getenv('token'))
