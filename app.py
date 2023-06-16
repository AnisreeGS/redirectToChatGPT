from flask import Flask, render_template, request,jsonify
import openai
openai.api_key = "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"


app = Flask(__name__)

@app.route("/ask", methods=['POST'])
def ask():
    question = request.json['question']
    print("inside ask - question",question)
    print("inside ask",request)
    response = openai.Completion.create(
        engine="davinci",
        # prompt=f"Q: {question}\nA:",
        prompt = f"A:",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )
    # answer = response
    answer = response.choices[0].text.strip()
    returnedAnswer = jsonify(answer)
    print("answer : " ,response)
    return returnedAnswer
    # question = request.body["question"]
    # answer = ask_chatgpt(question)
    # return render_template("answer.html", question=question, answer=answer)
    #return "true"

if __name__ =="__main__":
    app.run(debug=True)
