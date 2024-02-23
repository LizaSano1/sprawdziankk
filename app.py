from flask import Flask, request, jsonify
from sprawdzian import item_service

app = Flask(__name__)

@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(item_service.get_all_items())

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = item_service.get_item_by_id(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'age', 'group']):
        return jsonify({'error': 'Invalid data'}), 400

    item = item_service.create_item(data)
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    data = request.get_json()
    item = item_service.update_item(item_id, data)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = item_service.delete_item(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
