from flask import Flask, request, jsonify, render_template, session

app = Flask(__name__)

class Task:
    def __init__(self, id, title, difficulty, completed=False):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.completed = completed

tasks = []

current_mood = '평범'  # 기본값

@app.route('/')
def index():
    sorted_tasks = sort_tasks_by_mood(current_mood)
    return render_template('index.html', tasks=sorted_tasks, mood=current_mood)

# 할 일 추가
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    new_id = len(tasks) + 1
    new_task = Task(new_id, data['title'], data['difficulty'])
    tasks.append(new_task)
    return jsonify(new_task.__dict__), 201

# 목록보기
@app.route('/tasks', methods=['GET'])
def get_tasks():
    sorted_tasks = sort_tasks_by_mood(current_mood)
    return jsonify([task.__dict__ for task in sorted_tasks])

# 할 일 삭제
@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return jsonify({"message": "Task deleted"}), 200

# 완료 / 미완료 정렬
@app.route('/filter_tasks', methods=['GET'])
def filter_tasks():
    sorted_tasks = sorted(tasks, key=lambda x: x.completed)
    return jsonify([task.__dict__ for task in sorted_tasks])

@app.route('/set_mood', methods=['POST'])
def set_mood():
    global current_mood
    data = request.get_json()
    mood = data.get('mood')
    if mood in ['좋음', '평범', '나쁨']:
        current_mood = mood
        return jsonify({"message": f"Mood set to {mood}"}), 200
    else:
        return jsonify({"message": "Invalid mood"}), 400

# 기분 정렬
def sort_tasks_by_mood(mood):
    if mood == '좋음':
        return sorted(tasks, key=lambda task: {'hard': 0, 'medium': 1, 'easy': 2}[task.difficulty])
    elif mood == '나쁨':
        return sorted(tasks, key=lambda task: {'easy': 0, 'medium': 1, 'hard': 2}[task.difficulty])
    else:  # '평범'
        return sorted(tasks, key=lambda task: {'medium': 0, 'hard': 1, 'easy': 2}[task.difficulty])

# 키워드 검색
@app.route('/search', methods=['GET'])
def search_tasks():
    keyword = request.args.get('keyword', '').lower()
    filtered_tasks = [task for task in tasks if keyword in task.title.lower()]
    return jsonify([task.__dict__ for task in filtered_tasks]), 200

# 체크박스
@app.route('/toggle_complete/<int:task_id>', methods=['POST'])
def toggle_complete(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = not task.completed
            return jsonify({"message": "Task completion toggled"}), 200
    return jsonify({"message": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

