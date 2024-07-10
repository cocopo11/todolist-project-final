from flask import Flask, render_template, request

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
    return render_template('index.html', tasks=tasks)

@app.route('/search', methods=['GET'])
def search():
    '''
    팀원 4: 키워드 검색 기능
    '''
    # 키워드 검색 로직 구현 필요
    pass

if __name__ == '__main__':
    app.run(debug=True)

