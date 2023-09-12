from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=["POST"])
def formant_event():
    event = request.get_json()
    print(event["payload"]["message"])
    print(event["payload"]["value"])
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)