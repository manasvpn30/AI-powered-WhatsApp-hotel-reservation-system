from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Backend is running!"

@app.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():
    data = request.json
    print("Incoming message:", data)

    return jsonify({
        "status": "received"
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
