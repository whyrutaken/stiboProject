from flask import render_template
from app import app
from openai import OpenAI

@app.route("/")
@app.route("/index")
def index():
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Write a poem about web development.",
            },
        ],
    )

    return completion.choices[0].message.content




