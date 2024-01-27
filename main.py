# import os
# from openai import OpenAI

# client = OpenAI(
#     api_key=""
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "The dog says "  
#         }
#     ],
#     model="gpt-3.5-turbo-1106",
# )

import openai

openai.api_key = ""

returnMsg = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "In a single word, what is the color of a pickle?"}
    ],
    max_tokens=100,
)

# print(chat_completion.choices[0])
print(returnMsg)