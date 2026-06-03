from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

urls = {}

@app.route('/')
def home():

    url = request.args.get("url")
    short_url = ""
    message = ""

    if url:

        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        urls[code] = url

        short_url = f"http://127.0.0.1:5000/{code}"

    elif "url" in request.args:

        message = "Please enter a URL"

    return f'''
    <html>
    <head>
        <title>Simple URL Shortener</title>

        <style>

            body {{
                background: linear-gradient(135deg, #667eea, #764ba2);
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}

            .card {{
                background: white;
                padding: 40px;
                border-radius: 15px;
                width: 500px;
                text-align: center;
                box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
            }}

            input {{
                width: 90%;
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 8px;
            }}

            button {{
                margin-top: 15px;
                padding: 12px 25px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                background: #667eea;
                color: white;
                font-size: 16px;
            }}

            .result {{
                margin-top: 20px;
                background: #f4f4f4;
                padding: 15px;
                border-radius: 8px;
            }}

            a {{
                word-break: break-all;
            }}

        </style>

    </head>

    <body>

        <div class="card">

            <h1>🔗 Simple URL Shortener</h1>

            <form>

                <input
                type="text"
                name="url"
                placeholder="Paste your long URL here">

                <br>

                <button>Shorten URL</button>

            </form>

            <p>{message}</p>

            <div class="result">

                <b>Short URL:</b>

                <br><br>

                <a href="{short_url}" target="_blank">{short_url}</a>

            </div>

            <br>

            <small>Created by Nivedita</small>

        </div>

    </body>
    </html>
    '''

@app.route('/<code>')
def shortener(code):

    if code in urls:
        return redirect(urls[code])

    return "URL Not Found"

app.run()