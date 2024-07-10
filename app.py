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

@app.route('/filter_tasks', methods=['GET'])
def filter_tasks():
    """
    팀원 2: 할 일 완료/미완료 상태에 따른 정렬 기능
    """
    sorted_tasks = sorted(tasks, key=lambda x: x.completed)
    return jsonify([task.__dict__ for task in sorted_tasks])

if __name__ == '__main__':
    app.run(debug=True)
