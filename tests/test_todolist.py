import datetime
from todolist_utils import add_task, remove_task


def test_add_valid_task():
    tasks = []
    result = add_task(tasks, "Réviser le module", datetime.date.today())
    assert result == True
    assert len(tasks) == 1


def test_add_empty_task():
    tasks = []
    result = add_task(tasks, "", datetime.date.today())
    assert result == False
    assert len(tasks) == 0


def test_add_duplicate_task():
    tasks = [{"task": "Réviser le module", "done": False, "due_date": datetime.date.today()}]
    result = add_task(tasks, "Réviser le module", datetime.date.today())
    assert result == False
    assert len(tasks) == 1


def test_task_lifecycle():
    tasks = []
    add_task(tasks, "Faire le TP", datetime.date.today())
    assert len(tasks) == 1
    tasks[0]["done"] = True
    assert tasks[0]["done"] == True
    remove_task(tasks, "Faire le TP")
    assert len(tasks) == 0


def test_no_duplicate_regression():
    tasks = []
    add_task(tasks, "Projet maintenance", datetime.date.today())
    add_task(tasks, "Projet maintenance", datetime.date.today())
    assert len(tasks) == 1
