import os
import openai
from flask import Flask, request, render_template

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET","POST"))
def openai_app():
    if request.method == "POST":
        text = request.form["text"]
        color = request.form["color"]
        number = request.form["number"]
        response = openai.Image.create(
            prompt=generate_prompt(text,color),
            n=min(int(number), 5),
            size='256x256'
        )

        return render_template("index.html", result=response)

    return render_template("index.html")

def generate_prompt(text, color):
    return "Modern, symmetrical, balanced, centered, professional-looking, letter mark logo that incorporates the company name: \"{}\", {} color".format(text, color)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050)