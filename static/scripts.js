document.addEventListener("DOMContentLoaded", function () {
    fetchTasks();
    setActiveButton('all'); // 초기 로드 시 ALL 버튼에 선택된 클래스 추가
});

function addTask() {
    const title = document.getElementById('task-title').value;
    const difficulty = document.getElementById('task-difficulty').value;

    fetch('/add_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, difficulty })
    })
    .then(response => response.json())
    .then(data => {
        fetchTasks();
        document.getElementById('task-title').value = '';
        document.getElementById('task-difficulty').selectedIndex = 0; // 기본 옵션으로 초기화
    })
    .catch(error => console.error('Error:', error));
}

function fetchTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(data => {
            renderTasks(data);
            setActiveButton('all'); // "ALL" 버튼에 selected 클래스 추가
        })
        .catch(error => console.error('Error:', error));
}

function renderTasks(tasks) {
    // 완료된 할 일은 목록의 끝으로 이동
    tasks.sort((a, b) => a.completed - b.completed);
    
    const tasksContainer = document.getElementById('tasks-container');
    tasksContainer.innerHTML = ''; // 기존 할 일 목록을 지웁니다
    tasks.forEach(task => {
        // 각 할 일을 위한 HTML 요소를 생성합니다
        const taskItem = document.createElement('div');
        taskItem.className = `task-item ${task.completed ? 'completed' : ''}`;
        taskItem.innerHTML = `
            <label class="checkbox-container">
                <input type="checkbox" ${task.completed ? 'checked' : ''} onclick="toggleComplete(${task.id})">
                <span class="checkmark"></span>
            </label>
            <div class="task-title-container">
                <div class="task-title">${task.title}</div>
            </div>
            <div class="delete-icon-container">
                <img src="/static/bin.png" class="delete-icon" onclick="deleteTask(${task.id})">
            </div>
        `;
        tasksContainer.appendChild(taskItem);
    });
}

function deleteTask(id) {
    fetch(`/delete_task/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        fetchTasks();
    })
    .catch(error => console.error('Error:', error));
}

function setMood(mood) {
    fetch('/set_mood', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ mood })
    })
    .then(response => response.json())
    .then(data => {
        fetchTasksAndSort(mood); // 기분 변경 시 할 일 목록 다시 로드
        setActiveMoodButton(mood); // 버튼 색상 변경
    })
    .catch(error => console.error('Error:', error));
}

function fetchTasksAndSort(mood) {
    fetch('/tasks')
    .then(response => response.json())
    .then(data => {
        const sortedTasks = sortTasksByMood(data, mood);
        renderTasks(sortedTasks);
    })
    .catch(error => console.error('Error:', error));
}

function sortTasksByMood(tasks, mood) {
    if (mood === '좋음') {
        return tasks.sort((a, b) => {
            const priority = { 'hard': 0, 'medium': 1, 'easy': 2 };
            return priority[a.difficulty] - priority[b.difficulty];
        });
    } else if (mood === '나쁨') {
        return tasks.sort((a, b) => {
            const priority = { 'easy': 0, 'medium': 1, 'hard': 2 };
            return priority[a.difficulty] - priority[b.difficulty];
        });
    } else { // '평범'
        return tasks.sort((a, b) => {
            const priority = { 'medium': 0, 'hard': 1, 'easy': 2 };
            return priority[a.difficulty] - priority[b.difficulty];
        });
    }
}

function filterTasks(status) {
    fetch('/filter_tasks')
    .then(response => response.json())
    .then(data => {
        const tasksContainer = document.getElementById('tasks-container');
        tasksContainer.innerHTML = '';
        let filteredTasks;
        if (status === 'progress') {
            filteredTasks = data.filter(task => !task.completed);
        } else if (status === 'completed') {
            filteredTasks = data.filter(task => task.completed);
        } else {
            filteredTasks = data;
        }
        filteredTasks.forEach(task => {
            const taskItem = document.createElement('div');
            taskItem.className = `task-item ${task.completed ? 'completed' : ''}`;
            taskItem.innerHTML = `
                <label class="checkbox-container">
                    <input type="checkbox" ${task.completed ? 'checked' : ''} onclick="toggleComplete(${task.id})">
                    <span class="checkmark"></span>
                </label>
                <div class="task-title-container">
                    <div class="task-title">${task.title}</div>
                </div>
                <div class="delete-icon-container">
                    <img src="/static/bin.png" class="delete-icon" onclick="deleteTask(${task.id})">
                </div>
            `;
            tasksContainer.appendChild(taskItem);
        });
        setActiveButton(status);
    })
    .catch(error => console.error('Error:', error));
}

function searchTasks() {
    const keyword = document.getElementById('search').value.toLowerCase();

    fetch(`/search?keyword=${keyword}`)
    .then(response => response.json())
    .then(data => {
        renderTasks(data);
    })
    .catch(error => console.error('Error:', error));
}

function toggleComplete(id) {
    fetch(`/toggle_complete/${id}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        fetchTasks();
    })
    .catch(error => console.error('Error:', error));
}

function setActiveButton(status) {
    const buttons = document.querySelectorAll('.menu span, .menu div');
    buttons.forEach(button => {
        button.classList.remove('selected');
    });

    if (status === 'all') {
        document.querySelector('.all').classList.add('selected');
    } else if (status === 'progress') {
        document.querySelector('.progress').classList.add('selected');
    } else if (status === 'completed') {
        document.querySelector('.completed').classList.add('selected');
    }
}

function setActiveMoodButton(mood) {
    const moodButtons = document.querySelectorAll('.tdmdlist div');
    moodButtons.forEach(button => {
        button.classList.remove('selected-mood');
    });

    if (mood === '좋음') {
        document.querySelector('.good').classList.add('selected-mood');
    } else if (mood === '평범') {
        document.querySelector('.soso').classList.add('selected-mood');
    } else if (mood === '나쁨') {
        document.querySelector('.bad').classList.add('selected-mood');
    }
}