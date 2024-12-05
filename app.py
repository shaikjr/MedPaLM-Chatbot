from flask import Flask, request, render_template
import openai

app = Flask(__name__)
openai.api_key = 'sk-vBuO7LW4JUqcOZZ0bLjEn0Fituo_y2JbB-JE4JVn1YT3BlbkFJa0TnZ1O3TZERF8iP0sKqGKsO5BRlgIBEglbsxZrGYA'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        document = request.form['document']
        question = request.form['question']
        answer = ask_question(document, question)
        return render_template('index.html', answer=answer)
    return render_template('index.html')

def ask_question(document, question):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Document: {document}"},
        {"role": "user", "content": f"Question: {question}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=200
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == '__main__':
    app.run(debug=True)
