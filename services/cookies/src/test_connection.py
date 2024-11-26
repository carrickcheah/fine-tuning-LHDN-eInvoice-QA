import json
from openai import OpenAI
import os
import pandas as pd
from pprint import pprint

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    project=os.environ.get("project id")
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain what is hello kitty in malay language."
        }
    ]
)

print(completion.choices[0].message)