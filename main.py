from creds import BOT_TOKEN, GUILD_ID
from discord import app_commands
from DBmethods import GetAllWeapons
import discord
import re


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        if not self.synced:
            await tree.sync()
            self.synced = True
        print("hello i'm alive")


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name='test', description='test the bot')
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'Hello {name}!')
for weapon in GetAllWeapons():
    list_of_chars = ['+', ' ', "'s", '.', '(', ')']
    pattern = '[' + ''.join(list_of_chars) + ']'
    weapon = re.sub(pattern, '', weapon).lower()

    @tree.command(name=weapon, description=weapon)
    async def self(interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f'Hello {name}! welcome to {command}')

client.run(BOT_TOKEN)
