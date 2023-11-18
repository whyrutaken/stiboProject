from flask import render_template, redirect, flash
from app import app
from app.forms import MessageForm
from openai import OpenAI

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": form.message.data,
                },
            ],
        )
        return render_template("index.html", form=form, answer=completion.choices[0].message.content)
    return render_template("index.html", form=form)




