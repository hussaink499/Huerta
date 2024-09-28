import os

from groq import Groq


def chat(input_msg) :
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_msg,
            }
        ],
        model="llama3-8b-8192",
    )

    return (chat_completion.choices[0].message.content)
