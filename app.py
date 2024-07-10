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
    keyword = request.args.get('keyword', '').strip()
    if keyword:
        filtered_tasks = [task for task in tasks if keyword in task.title]
    else:
        filtered_tasks = tasks

    return render_template('index.html', tasks=filtered_tasks, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)

'''
<!-- index.html 파일에 아래 추가 -->
<form action="/search" method="GET">
    <input type="text" name="keyword" placeholder="검색어 입력">
    <button type="submit">검색</button>
</form>

<ul>
    {% for task in tasks %}
    <li>{{ task.title }} - {{ task.difficulty }}</li>
    {% endfor %}
</ul>
'''