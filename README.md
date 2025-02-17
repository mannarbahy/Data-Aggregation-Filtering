# Transaction Aggregation API

## Overview
This Python script implements a Flask API that processes transaction data, allowing users to filter transactions by customer ID and aggregate total revenue.

## Approach

### Load Transactions
- The script loads transaction data from `data.json`.

### TransactionAggregator Class
- Filters transactions based on `customer_id`.
- Aggregates total revenue for each customer.

### Flask API
- **`/customer_details`**: Accepts an optional `customer_id` query parameter.
  - If provided, filters transactions for that customer.
  - Aggregates and returns the total revenue.

### CORS Handling
- Allows cross-origin requests using `Flask-CORS`.

## Running the API

### Prerequisites
- Ensure `data.json` exists in the same directory.
- Install dependencies:
  ```sh
  pip install flask flask-cors
  ```

### Running the Script
```sh
python app.py
```
### Running React app
```sh
npm start
```

### Accessing the Endpoint
```sh
http://127.0.0.1:5000/customer_details?customer_id=2001
```

