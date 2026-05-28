import logging

logging.basicConfig(level=logging.INFO)


def add_task(tasks, task, due_date):
    if task.strip() == "":
        logging.warning("Tentative d'ajout d'une tâche vide")
        return False

    if any(t["task"] == task for t in tasks):
        logging.warning("Tentative d'ajout d'un doublon : %s", task)
        return False

    tasks.append({"task": task, "done": False, "due_date": due_date})
    logging.info("Ajout d'une tâche : %s", task)
    return True


def remove_task(tasks, task_name):
    for t in tasks:
        if t["task"] == task_name:
            tasks.remove(t)
            logging.info("Suppression d'une tâche : %s", task_name)
            return True
    return False
