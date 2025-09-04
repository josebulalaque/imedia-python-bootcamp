# Initial dictionary of tasks
tasks = {
    "Alice": [
        {"title": "Fix bugs", "status": "ongoing", "priority": "critical"},
        {"title": "Write docs", "status": "todo", "priority": "medium"}
    ],
    "Bob": [
        {"title": "Update UI", "status": "done", "priority": "low"}
    ],
    "Charlie": [
        {"title": "Test code", "status": "todo", "priority": "high"}
    ]
}

def show_all_tasks(queue):
    """TODO: Add cards in other to the last parts of deck"""

def add_task(queue, user_name, task_name, status, priority):
    """TODO: Add new task to user with given status and priority"""

def update_task_status(queue, user_name, task_name, new_status):
    """TODO: Return list of task name for user"""

def list_user_tasks(queue, user_name):
    """TODO: Return list of task name for user"""

def get_priority_summary(queue):
    """TODO: Return dict of count (how many low, medium, high, etc.)"""

def get_user_stats(queue, user_name):
    """TODO: Return dict of stats (tasks held, tasks done, etc.)"""

def add_user(queue,user_name):
    """TODO: Add new user_name from queue (if not there)"""

def remove_user(queue,user_name):
    """TODO: Remove user_name from queue (if there)"""
