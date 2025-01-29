from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример данных
data = {
    "users": [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35}
    ]
}
@app.route('/')
def home():
    return 'Добро пожаловать на сайт!'

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Маршрут для получения всех пользователей
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data)

# Маршрут для получения конкретного пользователя по ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in data['users'] if user['id'] == user_id), None)
    if user is not None:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Маршрут для добавления нового пользователя
@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.json
    if 'name' in new_user and 'age' in new_user:
        new_user['id'] = len(data['users']) + 1
        data['users'].append(new_user)
        return jsonify(new_user), 201
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True)
