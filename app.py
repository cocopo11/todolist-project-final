from flask import Flask, render_template

app = Flask(__name__)

class Task:
    def __init__(self, id, title, difficulty, completed=False):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.completed = completed

tasks = []

@app.route('/add_task', methods=['POST'])
def add_task():
    """
    팀원 1: 할 일 추가 기능
    """
    data = request.get_json()
    new_id = len(tasks) + 1
    new_task = Task(new_id, data['title'], data['difficulty'])
    tasks.append(new_task)
    return jsonify(new_task.__dict__), 201