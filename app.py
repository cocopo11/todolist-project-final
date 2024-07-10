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
    return render_template('index.html', tasks=tasks)

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
    # 할 일 추가 로직 구현 필요
    pass

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    팀원 1: 할 일 목록 보기 기능
    """
    return jsonify([task.__dict__ for task in tasks])

    pass

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    팀원 1: 할 일 삭제 기능
    """
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return jsonify({"message": "Task deleted"}), 200
    # 할 일 삭제 로직 구현 필요
    pass

@app.route('/filter_tasks', methods=['GET'])
def filter_tasks():
    """
    팀원 2: 할 일 완료/미완료 상태에 따른 정렬 기능
    """
    for task in tasks:
        if task.id == task_id:
            task.completed = not task.completed
            return jsonify(task.__dict__)
    return jsonify({"message": "Task not found"}), 404
   

    # 할 일 필터링 로직 구현 필요
    pass

@app.route('/sort_tasks_by_mood', methods=['GET'])
def sort_tasks_by_mood():
    """
    팀원 3: 기분 선택에 따른 투두리스트 정렬 로직 구현
    """
    # 기분에 따른 정렬 로직 구현 필요

@app.route('/set_mood', methods=['POST'])
def set_mood():
    """
    팀원 3: 오늘의 기분 선택 기능
    """
    # 오늘의 기분 설정 로직 구현 필요

@app.route('/search', methods=['GET'])
def search():
    '''
    팀원 4: 키워드 검색 기능
    '''
    # 키워드 검색 로직 구현 필요
    pass



if __name__ == '__main__':
    app.run(debug=True)
