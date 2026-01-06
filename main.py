from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    value = request.args.get("value")

    if value == "1":
        return "HELLO"
    elif value == "2":
        return "BYE"
    else:
        return "Please pass value=1 or value=2 in the URL"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
