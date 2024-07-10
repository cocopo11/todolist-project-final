from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
     """
     팀원 1: 할 일 목록 보기 기능
     """
    # 할 일 목록 반환 로직 구현 필요
    pass
