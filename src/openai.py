import openai
from src import initbot


openai.api_key = initbot.config["OPENAI_API_KEY"] # Using key OPENAI_API_KEY, access the openai key found in your config file

async def respond(request):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=request,
        temperature=0.75,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        #stop=["\n"]
    )
    
    return response.choices[0].text

