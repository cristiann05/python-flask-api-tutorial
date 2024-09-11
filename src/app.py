from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista inicial de todos
todos = [
    {"label": "A dummy todo", "done": True},
    {"label": "Another dummy todo", "done": False}
]

# Ruta GET para obtener la lista de todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# Ruta POST para agregar un nuevo todo
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    
    todos.append(request_body)
    return jsonify(todos), 200

# Ruta DELETE para eliminar un todo por su posición
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    """
    Endpoint para eliminar un 'todo' por su posición.
    1. Verifica si la posición es válida.
    2. Elimina el 'todo' en la posición especificada.
    3. Devuelve la lista de 'todos' actualizada.
    """
    # Verificar si la posición es válida
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400
    
    # Eliminar el 'todo' en la posición especificada
    todos.pop(position)
    
    # Retornar la lista de 'todos' actualizada
    return jsonify(todos), 200

# Bloque para ejecutar el servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
