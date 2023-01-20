import discord
from discord import app_commands

def get_config():
    import json
    with open("config.json", "r") as jsonfile:
        data = json.load(jsonfile)
    return data   

config = get_config()


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents().default())
        self.tree = app_commands.CommandTree(self)
        self.activity = discord.Activity(type=discord.ActivityType.streaming, name="/cvletter")


# intents = discord.Intents.default()
# client = discord.Client(intents=intents)
# tree = app_commands.CommandTree(client)
# client.activity = discord.Activity(type=discord.ActivityType.streaming, name="/cvletter")

def initialize_bot():
    """Initialize PyGPT Bot Client"""
    client = aclient()
    from src import commands
    


    
    @client.event
    async def on_ready():
        await client.tree.sync()
        
    @client.tree.command(name="cvletter",description="Write a CV or Interest letter for a company")
    async def cvletter(interaction: discord.Interaction, *, company: str, skills: str, jobdesc: str):
        #await interaction.response.defer(ephemeral=False)
        user = interaction.user
        request = "Can you write me a cover letter for " + company + " covering how my skills in " + skills + " will help with things detailed in their job description, such as " + jobdesc + ". Also, please keep it to, at a maximum, 3 paragraphs."
        channel = interaction.channel
        await commands.send_chat(request,interaction)
        
    @client.tree.command(name="chat",description="Chat with ChatGPT!")
    async def chat(interaction: discord.Interaction, *, message:str):
        #await interaction.response.defer(ephemeral=False)
        user = interaction.user
        request = str(message)
        channel = interaction.channel
        await commands.send_chat(request,interaction)
    
    @client.tree.command(name="codeexplain",description="Let ChatGPT Explain a file uploaded on github to you!")
    async def codeexplain(interaction: discord.Interaction, *, message:str):
        user = interaction.user
        #request = commands.link_parse(str(message))
        await commands.link_parse(message,interaction)

    
    # Run client command response (Requires token to execute)
    client.run(config['discord_bot_token'])
