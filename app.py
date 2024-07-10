from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Task:
    def __init__(self, id, title, difficulty, completed=False):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.completed = completed

tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/complete_task/<int:task_id>', methods=['PATCH'])
def complete_task(task_id):
    """
    팀원 2: 할 일 완료 표시 기능
    """
    for task in tasks:
        if task.id == task_id:
            task.completed = not task.completed
            return jsonify(task.__dict__)
    return jsonify({"message": "Task not found"}), 404
   
if __name__ == '__main__':
    app.run(debug=True)
