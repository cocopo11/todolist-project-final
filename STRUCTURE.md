# STRUCTURE.md

## Program Structure

### Objects
1. **Task**
   - Represents a to-do item with a title, difficulty, and completion status.

### Procedures and Functions

1. **index()**
   - Renders the main page with the list of tasks.

2. **get_tasks()**
   - Returns the list of all tasks as a JSON response.

3. **add_task()**
   - Adds a new task with a title and difficulty.

4. **delete_task(task_id)**
   - Deletes a task by its ID.

5. **complete_task(task_id)**
   - Toggles the completion status of a task by its ID.

6. **filter_tasks()**
   - Filters tasks based on their completion status.

7. **set_mood()**
   - Sets the user's mood for the day.

8. **sort_tasks_by_mood()**
   - Sorts tasks based on the user's mood.

9. **search_tasks()**
   - Searches tasks by a keyword in their title.