import os
from flask import Flask, request, jsonify, send_from_directory

try:
    import openai
    OPENAI_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_KEY:
        openai.api_key = OPENAI_KEY
        HAVE_OPENAI = True
    else:
        HAVE_OPENAI = False
except ImportError:
    HAVE_OPENAI = False

app = Flask(__name__)

@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json(force=True)
    message = data.get('message', '')
    if HAVE_OPENAI:
        resp = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': message}]
        )
        reply = resp.choices[0].message.content.strip()
    else:
        reply = f"You said: {message} (OpenAI not configured)"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
