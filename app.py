from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "project": "OC CI/CD Final Project — Python Task Manager",
        "message": "Application is running"
    })


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    print("Starting OC CI/CD application", flush=True)
    print("========== SERVICERUNNING ==========", flush=True)
    print("Listening on port 8000", flush=True)
    app.run(host="0.0.0.0", port=8000)
