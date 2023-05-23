from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"]
    answer = ask_chatgpt(question)
    return render_template("answer.html", question=question, answer=answer)

if __name__ =="__main__":
    app.run(port="5000")
