import discord
from discord import app_commands
from creds import BOT_TOKEN, GUILD_ID
from commandReader import returnCommands


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        if not self.synced:
            await tree.sync()
            self.synced = True


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name='info', description='gives info about weapons')
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'Hello {name}!')

client.run(BOT_TOKEN)
