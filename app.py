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
    # 할 일 완료 표시 로직 구현 필요
    pass

if __name__ == '__main__':
    app.run(debug=True)
