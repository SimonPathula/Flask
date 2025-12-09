from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id" : 1, "task" : "Drink Water"},
    {"id" : 2, "task" : "Do work"}
]

@app.route("/")
def welcome():
    return "Welcome to the home page"

@app.route("/items")
def get_items():
    return jsonify(items)

@app.route("/items/<int:id>", methods = ['GET'])
def get_item(id):
    found = None
    for i in items:
        if i["id"] == id:
            found = i
            break
    if found is None:
        return jsonify({"Error": "Item not found"}), 404
    return jsonify(found)

@app.route("/items", methods = ['POST'])
def create_item():
    data = request.json
    if not data or "task" not in data:
        return jsonify({"Error":"Invalid Entry"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "task": data["task"]
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route("/items/<int:id>", methods = ['PUT'])
def update_item(id):
    item = next((item for item in items if item["id"] == id), None)
    if item is None:
        return jsonify({"Error": "No such item is there"})
    data = request.json
    if not data or "task" not in data:
        return jsonify({"Error":"Invalid Entry"})
    item["task"] = data["task"]

    return jsonify(item)

@app.route("/items/<int:id>", methods = ["DELETE"])
def delete_item(id):
    item = next((item for item in items if item["id"] == id), None)
    if item is None:
        return jsonify({"Error": "No such item is there"})
    
    items.remove(item)
    return jsonify({"result": "Item deleted"})


if __name__ == '__main__':
    app.run(debug=True)