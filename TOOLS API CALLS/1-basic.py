import os

from openai import OpenAI
 
# USING API KEYS SAFELY -> https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)