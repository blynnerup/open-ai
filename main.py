import os
from openai import OpenAI

client = OpenAI(
    api_key=""
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "The dog says "  
        }
    ],
    model="gpt-3.5-turbo-1106",
)

print(chat_completion.choices[0])