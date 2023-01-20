from src import openai
import discord
import base64






async def send_chat(msg: str, interaction: discord.Interaction):
    """Responds to an interaction (discord slash command), sending a chat message (or multiple messages, if message is longer than discord's character limit.
    Requires: interaction is a valid discord interaction (valid interaction objects carry data such as server and channel id, which we need in order to respond in the correct location)
    Requires: msg is a valid string object
    """
    await interaction.response.defer(ephemeral=False) # This way, discord shows a 'PyGPT is thinking' message until the rest of the function is complete
    
    try:
        response = await openai.respond(msg) # Creates string with response from openai
        print(response)
        if len(response) > 1984: # Discord character limit is 2000; split message if more than 2000 (allowing for words extending longer)
            for i in [response[j:j+1984] for j in range(0,len(response),1984)]:
                await interaction.followup.send(i)
        else:
            await interaction.followup.send(response)
    except Exception:
        await interaction.followup.send("Error!")

async def send_chat_response(msg: str, request:str, interaction: discord.Interaction):
    """Responds to an interaction, and sends a response including the original message in the reply. Helpful for things such as explaining blocks of code,
    where instead of just gettign a response explaining the code, the bot will show the code and then ChatGPT's response"""
    
    # print(msg)
    await interaction.response.defer(ephemeral=False)
    response = await openai.respond(msg) # Creates string with response from openai
    # print(response)
    try: #
        """
        This code is broken into two blocks: request and response; this is so that when the followup is sent in the response block, it will reply as a followuo
        to itself, linking you back to the code it is explaining
        """
        if len(request) > 1984: # Discord character limit is 2000; split message if more than 2000 (allowing for words extending longer)
            for i in [request[j:j+1984] for j in range(0,len(request),1984)]:
                await interaction.followup.send(i)
        else:
            await interaction.followup.send(request)

        if len(response) > 1984: # Discord character limit is 2000; split message if more than 2000 (allowing for words extending longer)
            for i in [response[j:j+1984] for j in range(0,len(response),1984)]:
                await interaction.followup.send(i)
        else:
            await interaction.followup.send(response)
    except Exception:
        await interaction.followup.send("Error!")
    

async def link_parse(msg: str, interaction: discord.Interaction):
    """Parses a githublink for it's code.
    Requires: link is in the form "https://github.com/jonathandlee/PyGPT/blob/master/src/openai.py"
    """
    import requests
    print(msg)
    try:
        #msg.index("github.com")
        msg = msg.replace("github.com","raw.githubusercontent.com")
        msg = msg.replace("blob","") 
        msg = requests.get(msg).text
        #print(msg)
        
        code = "Please explain the following code:\n"+ msg
        msg = "Original Code: \n ```" + msg + "```"
        
        
        await send_chat_response(code,msg,interaction)
    except Exception:
        await interaction.followup.send("Invalid link")


    



    #response = await openai.respond(msg)

    







    





