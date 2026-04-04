import logging
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Configure in-memory storage and logging
users_db = {}
transactions_log = []
logging.basicConfig(level=logging.INFO)

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint for load balancer health checks."""
    return jsonify({"status": "healthy"}), 200

@app.route('/user', methods=['POST'])
def create_user():
    """Create a new user account."""
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('name')

    if not user_id or not name:
        return jsonify({"error": "user_id and name are required"}), 400

    if user_id in users_db:
        return jsonify({"error": "User already exists"}), 409

    users_db[user_id] = {"name": name, "balance": 0}
    app.logger.info(f"User created: {user_id}")
    return jsonify(users_db[user_id]), 201

@app.route('/transaction', methods=['POST'])
def simulate_transaction():
    """Simulate a financial transaction."""
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')

    if not user_id or amount is None:
        return jsonify({"error": "user_id and amount are required"}), 400

    user = users_db.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Simulate transaction logic
    new_balance = user['balance'] + amount
    user['balance'] = new_balance

    # Log the transaction
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "amount": amount,
        "new_balance": new_balance
    }
    transactions_log.append(log_entry)
    app.logger.info(f"Transaction processed: {log_entry}")

    return jsonify(log_entry), 201

if __name__ == '__main__':
        import os
        port = int(os.environ.get('PORT', 5001))
        app.run(host='0.0.0.0', port=port) 