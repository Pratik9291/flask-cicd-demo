from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Docker image push n pull successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
