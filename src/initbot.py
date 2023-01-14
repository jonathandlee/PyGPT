import discord
from discord import app_commands




import os

def get_config():
    import json


    with open("config.json", "r") as jsonfile:
        data = json.load(jsonfile)
    return data   

config = get_config()


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def initialize_bot():
    from src import commands

    @client.event
    async def ready():
        await tree.sync()

    @tree.command(name="cvletter",description="Write a CV or Interest letter for a company")
    async def cvletter(interaction: discord.Interaction, *, company: str, skills: str, jobdesc: str):
        #await interaction.response.defer(ephemeral=False)
        user = interaction.user
        request = "Can you write me a cover letter for " + company + " covering how my skills in " + skills + " will help with things detailed in their job description, such as " + jobdesc + ". Also, please keep it to, at a maximum, 3 paragraphs."
        channel = interaction.channel
        await commands.send_chat(request,interaction)
        
    @tree.command(name="chat",description="Chat with ChatGPT!")
    async def chat(interaction: discord.Interaction, *, message:str):
        #await interaction.response.defer(ephemeral=False)
        user = interaction.user
        request = str(message)
        channel = interaction.channel
        await commands.send_chat(request,interaction)
    client.run(config['discord_bot_token'])





    # if __name__ == '__initbot__':
    #     class discordclient(discord.Client):
    #         def __init__(self) -> None:
    #             super().__init__(intents=discord.Intents.default())
    #             self.tree = app_commands.CommandTree(self)
    #             self.activity = discord.Activity(type=discord.ActivityType.watching, name="/chat | /help")
    #     client = discordclient

    #     @client.event
    #     async def ready():

