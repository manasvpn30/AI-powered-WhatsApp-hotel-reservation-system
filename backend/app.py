from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get('Body')
    sender = request.form.get('From')

    print("Message:", incoming_msg)
    print("From:", sender)

    resp = MessagingResponse()
    resp.message("Hi 👋 I can help you book a room. How can I assist you?")

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
