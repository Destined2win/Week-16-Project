
# from flask import Flask, jsonify, request
# from models import Task
# from authentication import authenticate

# app = Flask(__name__)

# # Dummy data to store tasks
# tasks = []

# # Error handling decorator
# def handle_errors(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500
#     return wrapper

# # API endpoints

# # Create a new task
# @app.route('/tasks', methods=['POST'])
# @authenticate  # Add authentication decorator
# @handle_errors  # Add error handling decorator
# def create_task():
#     data = request.get_json()
#     if 'title' not in data or 'description' not in data:
#         raise ValueError('Title and description are required fields.')
    
#     new_task = Task(id=len(tasks) + 1, title=data['title'], description=data['description'])
#     tasks.append(new_task)
    
#     return jsonify({'task': new_task.__dict__}), 201

# # Retrieve all tasks
# @app.route('/tasks', methods=['GET'])
# @authenticate
# @handle_errors
# def get_tasks():
#     return jsonify({'tasks': [task.__dict__ for task in tasks]})

# # Retrieve a specific task by ID
# @app.route('/tasks/<int:task_id>', methods=['GET'])
# @authenticate
# @handle_errors
# def get_task(task_id):
#     task = next((task for task in tasks if task.id == task_id), None)
#     if task:
#         return jsonify({'task': task.__dict__})
#     raise ValueError('Task not found.')

# # Update an existing task
# @app.route('/tasks/<int:task_id>', methods=['PUT'])
# @authenticate
# @handle_errors
# def update_task(task_id):
#     task = next((task for task in tasks if task.id == task_id), None)
#     if task:
#         data = request.get_json()
#         task.title = data.get('title', task.title)
#         task.description = data.get('description', task.description)
#         task.completed = data.get('completed', task.completed)
#         return jsonify({'task': task.__dict__})
#     raise ValueError('Task not found.')

# # Delete a task
# @app.route('/tasks/<int:task_id>', methods=['DELETE'])
# @authenticate
# @handle_errors
# def delete_task(task_id):
#     global tasks
#     tasks = [task for task in tasks if task.id != task_id]
#     return jsonify({'message': 'Task deleted successfully'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)



app.py
from flask import Flask, jsonify, request
from models import Task

app = Flask(__name__)
tasks = []  # In-memory data store for simplicity; replace with a database in a real-world scenario

# Step 4: Implement Endpoint Logic

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' not in data or 'description' not in data or 'completed' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_task = Task(
        id=len(tasks) + 1,
        title=data['title'],
        description=data['description'],
        completed=data['completed']
    )
    tasks.append(new_task)
    return jsonify({'message': 'Task created successfully'}), 201

# Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify({'tasks': [task.to_dict() for task in tasks]})

# Retrieve a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.to_dict())

# Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    return jsonify({'message': 'Task updated successfully'})

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)




