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
