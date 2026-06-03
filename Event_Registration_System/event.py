from flask import Flask, request

app = Flask(__name__)

participants = []

@app.route('/')
def home():

    name = request.args.get("name", "").strip()

    if name and name not in participants:
        participants.append(name)

    participant_list = ""

    for person in participants:
        participant_list += f"<tr><td>{person}</td></tr>"

    count = len(participants)

    return f'''
    <html>

    <head>

    <title>Event Registration System</title>

    <style>

    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    body {{
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg,#0f172a,#1e293b,#111827);
    }}

    .card {{
        width: 700px;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 20px;
        padding: 35px;
        color: white;
        box-shadow: 0 0 30px rgba(0,255,255,0.15);
    }}

    h1 {{
        text-align: center;
        margin-bottom: 20px;
    }}

    .counter {{
        text-align: center;
        margin-bottom: 20px;
        font-size: 20px;
        color: #38bdf8;
    }}

    input {{
        width: 100%;
        padding: 14px;
        border-radius: 10px;
        border: none;
        margin-bottom: 15px;
        font-size: 16px;
    }}

    button {{
        width: 100%;
        padding: 14px;
        border: none;
        border-radius: 10px;
        font-size: 16px;
        cursor: pointer;
        background: #06b6d4;
        color: white;
        font-weight: bold;
    }}

    button:hover {{
        transform: scale(1.02);
    }}

    .table-box {{
        margin-top: 25px;
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 15px;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
    }}

    th {{
        color: #38bdf8;
        padding-bottom: 10px;
        text-align: left;
    }}

    td {{
        padding: 10px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}

    .footer {{
        margin-top: 20px;
        text-align: center;
        color: #94a3b8;
    }}

    </style>

    </head>

    <body>

        <div class="card">

            <h1>🚀 Event Registration Dashboard</h1>

            <div class="counter">

                Registered Participants: {count}

            </div>

            <form>

                <input
                type="text"
                name="name"
                placeholder="Enter participant name">

                <button>Register Participant</button>

            </form>

            <div class="table-box">

                <table>

                    <tr>
                        <th>Participant Name</th>
                    </tr>

                    {participant_list}

                </table>

            </div>

            <div class="footer">

                Created by Nivedita

            </div>

        </div>

    </body>

    </html>
    '''

app.run()