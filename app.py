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

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    팀원 1: 할 일 목록 보기 기능
    """
    return jsonify([task.__dict__ for task in tasks])

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    팀원 1: 할 일 삭제 기능
    """
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return jsonify({"message": "Task deleted"}), 200

@app.route('/filter_tasks', methods=['GET'])
def filter_tasks():
    """
    팀원 2: 할 일 완료/미완료 상태에 따른 정렬 기능
    """
    sorted_tasks = sorted(tasks, key=lambda x: x.completed)
    return jsonify([task.__dict__ for task in sorted_tasks])
    for task in tasks:
        if task.id == task_id:
            task.completed = not task.completed
            return jsonify(task.__dict__)
    return jsonify({"message": "Task not found"}), 404

@app.route('/set_mood', methods=['POST'])
def set_mood():
    """
    팀원 3: 오늘의 기분 선택 기능
    """
    global current_mood
    data = request.get_json()
    mood = data.get('mood')
    if mood in ['좋음', '평범', '나쁨']:
        current_mood = mood
        return jsonify({"message": f"Mood set to {mood}"}), 200
    else:
        return jsonify({"message": "Invalid mood"}), 400

def sort_tasks_by_mood(mood):
    if mood == '좋음':
        return sorted(tasks, key=lambda task: {'hard': 0, 'medium': 1, 'easy': 2}[task.difficulty])
    elif mood == '나쁨':
        return sorted(tasks, key=lambda task: {'easy': 0, 'medium': 1, 'hard': 2}[task.difficulty])
    else:  # '평범'
        return sorted(tasks, key=lambda task: {'medium': 0, 'hard': 1, 'easy': 2}[task.difficulty])

@app.route('/search', methods=['GET'])
def search_tasks():
    """
    팀원 4: 키워드 검색 기능
    """
    keyword = request.args.get('keyword', '').lower()
    filtered_tasks = [task for task in tasks if keyword in task.title.lower()]
    return jsonify([task.__dict__ for task in filtered_tasks]), 200

if __name__ == '__main__':
    app.run(debug=True)

