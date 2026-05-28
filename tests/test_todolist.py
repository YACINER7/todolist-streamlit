import pytest
from core.todolist_utils import add_task, remove_task, mark_done


def test_ajout_tache_valide():
    tasks = []
    add_task(tasks, "Faire les courses", None)
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Faire les courses"
    assert tasks[0]["done"] == False


def test_tache_vide_refusee():
    tasks = []
    with pytest.raises(ValueError):
        add_task(tasks, "   ", None)


def test_doublon_refuse():
    tasks = []
    add_task(tasks, "Faire les courses", None)
    with pytest.raises(ValueError):
        add_task(tasks, "Faire les courses", None)


def test_cycle_complet():
    tasks = []
    add_task(tasks, "Faire les courses", None)
    mark_done(tasks, 0)
    assert tasks[0]["done"] == True
    remove_task(tasks, "Faire les courses")
    assert len(tasks) == 0


def test_regression_anti_doublon():
    tasks = []
    add_task(tasks, "Tâche A", None)
    add_task(tasks, "Tâche B", None)
    with pytest.raises(ValueError):
        add_task(tasks, "Tâche A", None)
    assert len(tasks) == 2
