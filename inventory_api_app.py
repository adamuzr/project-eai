from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated inventory
inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

@app.route("/order", methods=["POST"])
def place_order():
    data = request.get_json()
    product = data.get("product")
    quantity = data.get("quantity")

    if not product or quantity is None:
        return jsonify({"status": "error", "message": "Missing product or quantity"}), 400

    if product not in inventory:
        return jsonify({"status": "error", "message": "Product not found"}), 404

    if inventory[product] < quantity:
        return jsonify({"status": "error", "message": "Not enough stock"}), 400

    inventory[product] -= quantity
    return jsonify({"status": "success", "message": f"Order placed for {quantity} {product}(s)."}), 200

if __name__ == "__main__":
    app.run(debug=True)
