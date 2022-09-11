import discord
from discord import app_commands
from creds import BOT_TOKEN,GUILD_ID
from commandReader import returnCommands

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced=False
    async def on_ready(self):
        if not self.synced:
            #await tree.sync(guild=discord.Object(id=GUILD_ID))
            await tree.sync()
            self.synced=True
        print("hello i'm alive")


client=aclient()
tree=app_commands.CommandTree(client)

for command in returnCommands():
    @tree.command(name=command,description=command)
    async def self(interaction: discord.Interaction,name:str):
        await interaction.response.send_message(f'Hello {name}! welcome to {command}')

client.run(BOT_TOKEN)