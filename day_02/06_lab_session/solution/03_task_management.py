def show_all_tasks(queue):
    """Print all tasks grouped by user"""
    for user, tasks in queue.items():
        print(f"\n{user}'s tasks:")
        for task in tasks:
            print(f"  - {task['title']} [{task['status']}, {task['priority']}]")


def add_task(queue, user_name, task_name, status, priority):
    """Add new task to user with given status and priority"""
    if user_name not in queue:
        print(f"User '{user_name}' not found.")
        return
    queue[user_name].append({
        "title": task_name,
        "status": status,
        "priority": priority
    })


def update_task_status(queue, user_name, task_name, new_status):
    """Update the status of a task for a specific user"""
    if user_name not in queue:
        print(f"User '{user_name}' not found.")
        return
    for task in queue[user_name]:
        if task['title'] == task_name:
            task['status'] = new_status
            return
    print(f"Task '{task_name}' not found for user '{user_name}'.")


def list_user_tasks(queue, user_name):
    """Return list of task titles for a user"""
    if user_name not in queue:
        print(f"User '{user_name}' not found.")
        return []
    return [task['title'] for task in queue[user_name]]


def get_priority_summary(queue):
    """Return dict of count of each priority (low, medium, etc.)"""
    summary = {}
    for tasks in queue.values():
        for task in tasks:
            p = task['priority']
            summary[p] = summary.get(p, 0) + 1
    return summary


def get_user_stats(queue, user_name):
    """Return dict of stats (tasks total, tasks done, etc.)"""
    if user_name not in queue:
        print(f"User '{user_name}' not found.")
        return {}
    stats = {"total": 0, "done": 0, "todo": 0, "ongoing": 0}
    for task in queue[user_name]:
        stats["total"] += 1
        status = task["status"]
        if status in stats:
            stats[status] += 1
    return stats


def add_user(queue, user_name):
    """Add new user to queue (if not already present)"""
    if user_name in queue:
        print(f"User '{user_name}' already exists.")
    else:
        queue[user_name] = []


def remove_user(queue, user_name):
    """Remove user from queue (if present)"""
    if user_name in queue:
        del queue[user_name]
    else:
        print(f"User '{user_name}' not found.")


def main():
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

    add_user(tasks, "Denki")
    add_task(tasks, "Denki", "Zap things", "todo", "high")
    update_task_status(tasks, "Denki", "Zap things", "done")
    print(get_user_stats(tasks, "Denki"))


main()
