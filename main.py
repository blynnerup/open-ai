import os
from openai import OpenAI

client = OpenAI(
    api_key="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"
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