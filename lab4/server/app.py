import json
import os

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"


# === Вспомогательные функции ===

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_next_id(todos):
    return max([todo["id"] for todo in todos], default=0) + 1


def todo_to_dto(todo):
    return {
        "id": todo["id"],
        "name": todo["name"],
        "isComplete": todo["isComplete"]
    }


# === API ===

@app.route('/api/todoitems', methods=['GET'])
def get_todos():
    todos = load_data()
    return jsonify([todo_to_dto(todo) for todo in todos])


@app.route('/api/todoitems/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todos = load_data()
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo is None:
        return abort(404)
    return jsonify(todo_to_dto(todo))


@app.route('/api/todoitems', methods=['POST'])
def create_todo():
    todos = load_data()
    data = request.get_json()
    new_todo = {
        "id": get_next_id(todos),
        "name": data.get("name"),
        "isComplete": data.get("isComplete", False),
        "secret": data.get("secret", "")
    }
    todos.append(new_todo)
    save_data(todos)
    return jsonify(todo_to_dto(new_todo)), 201


@app.route('/api/todoitems/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todos = load_data()
    data = request.get_json()
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo is None:
        return abort(404)

    todo["name"] = data.get("name", todo["name"])
    todo["isComplete"] = data.get("isComplete", todo["isComplete"])
    save_data(todos)
    return '', 204


@app.route('/api/todoitems/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todos = load_data()
    new_todos = [item for item in todos if item["id"] != todo_id]
    if len(new_todos) == len(todos):
        return abort(404)
    save_data(new_todos)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=5000)
