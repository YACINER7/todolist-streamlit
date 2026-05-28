def add_task(tasks, task, due_date):
    if not task.strip():
        raise ValueError("La tâche ne peut pas être vide.")
    if any(t["task"].lower() == task.strip().lower() for t in tasks):
        raise ValueError("Cette tâche existe déjà.")
    tasks.append({"task": task.strip(), "done": False, "due_date": due_date})
    return tasks


def remove_task(tasks, task_name):
    tasks[:] = [t for t in tasks if t["task"] != task_name]
    return tasks


def mark_done(tasks, index):
    tasks[index]["done"] = True
    return tasks
