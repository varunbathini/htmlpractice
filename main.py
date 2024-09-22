from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def ping():
    return "ping sample"

@app.route("/home")
def sample_page():
    resp = Response("""
    <html>
    <body>
    <h1>This is a HTML based content</h1>
    </body>
    </html>
    """)
    return resp

app.run()