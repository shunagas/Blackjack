from flask import Flask, request, jsonify
from montecarlo import monte_carlo_simulation

app = Flask(__name__)

@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.json

    trials = int(data.get("trials", 10000))
    bankroll = int(data.get("bankroll", 100000))
    bet = int(data.get("bet", 1000))

    result = monte_carlo_simulation(trials, bankroll, bet, False, True)

    return jsonify({"result": "OK"})

@app.route("/")
def home():
    return "Blackjack API is running"

if __name__ == "__main__":
    app.run()
