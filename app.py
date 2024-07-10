from flask import Flask, render_template

app = Flask(__name__)

class Task:
    def __init__(self, id, title, difficulty, completed=False):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.completed = completed

tasks = []

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    팀원 1: 할 일 삭제 기능
    """
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)