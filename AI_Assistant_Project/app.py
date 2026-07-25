from flask import Flask, render_template, request
from prompts import *

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Process User Input
@app.route('/process', methods=['POST'])
def process():

    function = request.form['function']
    user_input = request.form['user_input']

    # Question Answering
    if function == "question":

        text = user_input.lower()

        if "python" in text:
            response = """Python is a high-level programming language.
It is simple, easy to learn, and widely used for web development,
Artificial Intelligence, Machine Learning, Data Science, and Automation."""

        elif "artificial intelligence" in text or "ai" in text:
            response = """Artificial Intelligence (AI) is the simulation of human intelligence by computers.
It enables machines to learn, reason, solve problems, and make decisions."""

        elif "prompt engineering" in text:
            response = """Prompt Engineering is the process of writing effective instructions (prompts)
to get accurate and useful responses from AI models."""

        elif "flask" in text:
            response = """Flask is a lightweight Python web framework used to build web applications
quickly and easily."""

        elif "html" in text:
            response = """HTML (HyperText Markup Language) is used to create the structure
of web pages."""

        else:
            response = f"""Question:
{user_input}

Thank you for your question.

Currently this offline AI Assistant contains answers for common topics like
Python, AI, Prompt Engineering, Flask and HTML."""

    # Text Summarization
    elif function == "summary":
        
        words = user_input.split()

        if len(words) > 50:
            response = " ".join(words[:50]) + "..."
        else:
            response = user_input

    # Creative Writing
    elif function == "creative":

        response = f"""Story Title: {user_input}

Once upon a time, there was a young student who never gave up.

With hard work, patience, and determination,
the student achieved every dream.

Moral:
Success comes to those who work hard and believe in themselves."""

    # Study Advice
    elif function == "advice":

        response = f"""Study Tips for {user_input}

1. Study every day for 2 hours.
2. Make short notes.
3. Revise regularly.
4. Solve previous year question papers.
5. Take short breaks.
6. Stay confident before exams."""

    else:
        response = "Invalid Choice"

    return render_template("result.html", result=response)


# Save Feedback
@app.route('/feedback', methods=['POST'])
def feedback():

    value = request.form['feedback']

    with open("feedback.txt", "a") as file:
        file.write(value + "\n")

    return "Thank you for your feedback!"


if __name__ == "__main__":
    app.run(debug=True)