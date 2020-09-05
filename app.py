from flask import Flask, request, render_template
from question_answering import get_answers

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/qa", methods=['POST'])
def echo():
    context = request.form['context']
    question = request.form['question']
    result = get_answers(context,question)

    return render_template('question_answering.html',context=context,question=question,result=result)


if __name__ == "__main__":
    app.run(debug='True')