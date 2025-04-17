from flask import Flask, request
import logging

app = Flask(__name__)

# confihure logging
logging.basicConfig(
    level=logging.INFO, # set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  #  format
)

@app.route("/", methods=["GET"])
def home():
    app.logger.info("Home route accessed from IP: %s", request.remote_addr)
    return "Welcome to Flask CI/CD project", 200

@app.errorhandler(404)
def not_found(e):
    app.logger.warning("404 error encountered at path: %s", request.path)
    return {"error": "Not Found"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)