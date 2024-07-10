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

@app.route('/sort_tasks_by_mood', methods=['GET'])
def sort_tasks_by_mood():
    """
    팀원 3: 기분 선택에 따른 투두리스트 정렬 로직 구현
    """
    # 기분에 따른 정렬 로직 구현 필요
    pass

if __name__ == '__main__':
    app.run(debug=True)
