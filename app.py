from flask import Flask, request, jsonify
from sprawdzian import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(user_service.get_all_users())

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(key in data for key in ['firstName', 'lastName', 'birthYear', 'group']):
        return jsonify({'error': 'Invalid data'}), 400

    user = user_service.create_user(data)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.get_json()
    user = user_service.update_user(user_id, data)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = user_service.delete_user(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
