# Chatflow

A minimal web interface for chatting with a large language model. By default it echoes your input unless an OpenAI API key is configured.

## Requirements

- Python 3
- Packages listed in `requirements.txt`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running

```bash
python server.py
```

Navigate to `http://localhost:5000` to start chatting.

Set the environment variable `OPENAI_API_KEY` to enable responses from OpenAI's API.

