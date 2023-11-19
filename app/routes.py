from flask import render_template
from app import app, openai_client


@app.route("/query/<message>")
def query_chatGPT(message):
    completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return completion.choices[0].message.content




@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")




