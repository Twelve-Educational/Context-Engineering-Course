import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GPT_KEY"),
    base_url=os.getenv("GPT_BASE") + "/",
)

input_search = "Can you return a list of recent youtube videos about current transfer rumours for Liverpool? Focus on popular fan channels rather than mainstream media. Make sure you give urls for up to 10 recent and relevant videos on this subject. They do not have to be in English. Do not ask me follow on questions, just make sure you get the video links."

response = client.responses.create(
    model=os.getenv("GPT_CHAT_MODEL"),
    tools=[{"type": "web_search_preview"}],
    input=input_search,
)

print(response.output_text)
