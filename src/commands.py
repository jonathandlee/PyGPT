from src import openai
import discord

async def send_chat(msg: str, interaction: discord.Interaction):
    print(msg)
    await interaction.response.defer(ephemeral=False)
    response = await openai.respond(msg) # Creates string with response from openai
    try:
        if len(response) > 1984: # Discord character limit is 2000; split message if more than 2000 (allowing for words extending longer)
            for i in [response[j:j+1984] for j in range(0,len(response),1984)]:
                await interaction.followup.send(i)
        else:
            await interaction.followup.send(response)
    except Exception:
        await interaction.followup.send("Error!")
    
    







    





