from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.router('/api/data', methods=['GET'])
def get_data():
    """Function to get and return list of data"""
    data = [
        {
            "Name": "Baby T-shirt",
            "Color": "Green",
            "Price": "N2000",
            "Description": "Green Baby T-shirt for babies from newborn to 24 months"
        },
        {
            "Name": "Baby Jumper",
            "Color": "Pink",
            "Price": "N2000",
            "Description": "Pink Baby Jumper for babies from newborn to 24 months"
        },
        {
            "Name": "Baby Bottle",
            "Color": "Blue",
            "Price": "N5000",
            "Description": "Green Baby Bottle for babies from newborn to 24 months"
        },
        {
            "Name": "Baby Teething Ring",
            "Color": "Nude",
            "Price": "N9000",
            "Description": "Nude Baby Teething Ring for babies from newborn to 24 months"
        },
    ]
    return jsonify(data)

@app.route('/api/products/<int: item_id', methods=['GET'])
def get_one_product(product_id):
    """Function to get and return only only one product"""
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"Message": "Item not found"}), 404
