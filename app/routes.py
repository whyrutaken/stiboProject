from flask import render_template, redirect, flash
from app import app
from app.forms import MessageForm
from openai import OpenAI


def query_chatGPT(data):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": data,
            },
        ],
    )
    return completion.choices[0].message.content


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        answer = query_chatGPT(form.message.data)
        return render_template("index.html", form=form, answer=answer)
    return render_template("index.html", form=form)




