from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to Flask CI/CD project", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
