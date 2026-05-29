from flask import Flask, request
import time

app = Flask(__name__)

VERIFY_TOKEN = "luna_verify_123"

@app.route("/", methods=["GET"])
def home():
    return "Bot attivo"

# Verifica webhook Instagram
@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return str(challenge), 200
    return "Errore verifica", 403


# Ricezione messaggi
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Messaggio ricevuto:", data)

    # simulazione risposta (poi mettiamo AI)
    time.sleep(5)

    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
