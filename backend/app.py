from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

with open("./data.json") as f:
    transactions = json.load(f)

class TransactionAggregator:
    def __init__(self, transactions):
        self.transactions = transactions

    def filter_by_customer(self, customer_id=None):

        if customer_id is None:
            return self.transactions

        filtered_transactions = []
        for t in self.transactions:
            if t["customer_id"] == customer_id:
                filtered_transactions.append(t)
        return filtered_transactions

    def aggregate_total_revenue(self, filtered_transactions):
            revenue_per_customer = {}
            for t in filtered_transactions:
                customer = t["customer_id"]
                if customer in revenue_per_customer:
                    revenue_per_customer[customer] += t["total_amount"]
                else:
                    revenue_per_customer[customer] = t["total_amount"]
            return revenue_per_customer

@app.route("/customer_details")
def customer_details():
    try:
        customer_id = request.args.get("customer_id", type=int)
        aggregator = TransactionAggregator(transactions)
        filtered_data = aggregator.filter_by_customer(customer_id)
        result = aggregator.aggregate_total_revenue(filtered_data)
        return jsonify(result) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500  

if __name__ == "__main__":
    app.run(debug=True)