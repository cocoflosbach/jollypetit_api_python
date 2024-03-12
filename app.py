"""API for Children's online store application"""

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
        {
            "Name": "Baby T-shirt",
            "Color": "Green",
            "Price": "N2000",
            "Description": "Green Baby T-shirt for babies from newborn to 24 months",
            "product_id": 1
        },
        {
            "Name": "Baby Jumper",
            "Color": "Pink",
            "Price": "N2000",
            "Description": "Pink Baby Jumper for babies from newborn to 24 months",
            "product_id": 2
        },
        {
            "Name": "Baby Bottle",
            "Color": "Blue",
            "Price": "N5000",
            "Description": "Green Baby Bottle for babies from newborn to 24 months",
            "product_id": 3
        },
        {
            "Name": "Baby Teething Ring",
            "Color": "Nude",
            "Price": "N9000",
            "Description": "Nude Baby Teething Ring for babies from newborn to 24 months",
            "product_id": 4
        },
    ]

users = [
    {
        "Username": "babygworl",
        "user_id": 1,
        "Password": "bbg123",
        "Email": "baby@ever.com",
        "Birthday": "02-02-1994"
    },
    {
        "Username": "rabbitbasket",
        "user_id": 2,
        "Password": "rabby",
        "Email": "rabbit@ever.com",
        "Birthday": "05-07-1992"
    },
    {
        "Username": "cakeworld",
        "user_id": 3,
        "Password": "cakey",
        "Email": "cakebabe@ever.com",
        "Birthday": "07-09-1991"
    },
]

@app.route('/products', methods=['GET'])
def get_products():
    """Function to get and return list of all data"""
    return jsonify(products)

@app.route('/api/products/<int: item_id', methods=['GET'])
def get_one_product(product_id):
    """Function to get and return only only one product"""
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"Message": "Item not found"}), 404

@app.route('/users', methods = ['GET'])
def get_users():
    """Function to get and return the list of all users"""
    return jsonify(users)

@app.route('/users/<int: item_id', methods = ['GET'])
def get_one_user(user_id):
    """Function to get and return only one product"""
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"Message": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
